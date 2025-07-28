B A C H E L O R T H E S I S

Embedded Debug Interface for Robots

vorgelegt von

Robin Mirow

MIN-Fakult¨at

Fachbereich Informatik

Technische Aspekte Multimodaler Systeme

Studiengang: Informatik

Matrikelnummer: 6946287

Erstgutachter: Dr. Andreas M¨ader

Zweitgutachter: M. Sc. Marc Bestmann

Abstract

Modern robot platforms consist of a multitude of sensors, servos, and other inter-
connected devices. Particularly in the case of robots that are designed to operate
independently, it is often required to diagnose problems with these devices without
connecting the robot to a dedicated computer.
This bachelor thesis describes the hardware layout and software implementation for
a microcontroller board with an LCD touchscreen that can be attached directly to
a robot. It continuously listens on an RS-485 bus using the ROBOTIS Dynamixel
Protocol 2.0 [ROBe] and displays detailed information about supported devices.
Other robot platforms using the same protocol would also work as long as they use
a bus compatible with a UART (Universal Asynchronous Receiver Transmitter)
interface.

Zusammenfassung

Moderne Roboterplattformen bestehen aus einer Vielzahl von Sensoren, Servomo-
toren und anderen miteinander verbundenen Ger¨aten. Insbesondere im Fall von
Robotern, die darauf ausgelegt sind unabh¨angig zu agieren, ist es oft notwendig
Probleme mit diesen Ger¨aten zu diagnostizieren ohne den Roboter an einen dedi-
zierten Computer anzuschließen.
Diese Bachelorarbeit beschreibt den Hardware-Aufbau und die Software-Imple-
mentation f¨ur eine Mikrocontrollerplatine mit einem LCD Touchscreen, die direkt
an einen Roboter montiert werden kann. Diese h¨ort kontinuierlich einen RS-485
Bus ab, der das ROBOTIS Dynamixel Protocol 2.0 [ROBe] verwendet, und zeigt
detailierte Informationen ¨uber unterst¨utzte Ger¨ate an.
Andere Roboterplattformen, die das gleiche Protokoll verwenden, w¨urden auch
funktionieren, solange sie einen Bus benutzen, der mit einer UART (Universal
Asynchronous Receiver Transmitter) Schnittstelle kompatibel ist.

Contents

Abstract

List of Figures

1 Introduction

1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 RoboCup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Thesis Goal

2 Related Work

iii

viii

1
1
2
4

5

3 Basics

7
7
3.1 RS-485 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 ROBOTIS Dynamixel Protocol 2.0 . . . . . . . . . . . . . . . . . .
7
3.3 Embedded Operating Systems . . . . . . . . . . . . . . . . . . . . . 16

17
4 Implementation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.1 Hardware
4.2 Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

5 Evaluation

39
5.1 Measurement Method . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.2 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

6 Discussion

57

7 Conclusion and Future Work

59
7.1 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
7.2 Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

Bibliography

61

v

List of Figures

1.1 The Wolfgang robot platform . . . . . . . . . . . . . . . . . . . . .
1.2 A RoboCup soccer game . . . . . . . . . . . . . . . . . . . . . . . .

2.1 The Pepper robot . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2
3

5

8
3.1 Generic packet layout . . . . . . . . . . . . . . . . . . . . . . . . . .
9
. . . . . . . . . . . . . . . . . . . . . . .
3.2 Ping instruction payloads
3.3 Read instruction payloads
9
. . . . . . . . . . . . . . . . . . . . . . .
3.4 Write instruction payloads . . . . . . . . . . . . . . . . . . . . . . . 10
. . . . . . . . . . . . . . . . . . . . 10
3.5 Reg Write instruction payloads
. . . . . . . . . . . . . . . . . . . . . . 10
3.6 Action instruction payloads
3.7 Factory Reset instruction payloads
. . . . . . . . . . . . . . . . . . 11
3.8 Reboot instruction payloads
. . . . . . . . . . . . . . . . . . . . . . 11
3.9 Clear instruction payloads . . . . . . . . . . . . . . . . . . . . . . . 11
3.10 Sync Read instruction payloads . . . . . . . . . . . . . . . . . . . . 12
3.11 Sync Write instruction payloads . . . . . . . . . . . . . . . . . . . . 13
3.12 Bulk Read instruction payloads
. . . . . . . . . . . . . . . . . . . . 14
3.13 Bulk Write instruction payloads . . . . . . . . . . . . . . . . . . . . 15

4.1 The STM32F7508-DK development board . . . . . . . . . . . . . . 18
4.2 Bootloader packet layout . . . . . . . . . . . . . . . . . . . . . . . . 20
4.3 Bootloader program ﬂow . . . . . . . . . . . . . . . . . . . . . . . . 21
4.4 Screenshot of the device overview . . . . . . . . . . . . . . . . . . . 26
4.5 Screenshot of the model overview . . . . . . . . . . . . . . . . . . . 27
4.6 Screenshot of the device details view . . . . . . . . . . . . . . . . . 28
4.7 Screenshot of the log view . . . . . . . . . . . . . . . . . . . . . . . 29
4.8 Layout of the DMA buﬀer . . . . . . . . . . . . . . . . . . . . . . . 31

5.1 Time per buﬀer and time between buﬀers for trace traﬃc with no

delay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

5.2 Time per buﬀer and time between buﬀers for trace traﬃc with 100 µs

delay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

5.3 Time per buﬀer and time between buﬀers for synthetic read/write

traﬃc with no delay . . . . . . . . . . . . . . . . . . . . . . . . . . 46

5.4 Time per buﬀer and time between buﬀers for synthetic read/write

traﬃc with 100 µs delay . . . . . . . . . . . . . . . . . . . . . . . . 48

vii

List of Figures

5.5 Time per buﬀer and time between buﬀers for synthetic ping traﬃc

with no delay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

5.6 Time per buﬀer and time between buﬀers for synthetic ping traﬃc

with 100 µs delay . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

viii

1 Introduction

As robots become cheaper and more popular for common tasks, they are frequently
used as independent platforms without signiﬁcant supporting infrastructure or
personnel. Because of this, it is important that robots are equipped with easy to
use interfaces to control them and diagnose problems. Touchscreen displays are
ideal for this use case, as they can be attached to any even surface and do not
require any specialized input devices.
This thesis implements an example of such an interface as a standalone microcon-
troller board that can be directly attached to a robot built on the Wolfgang robot
platform (see section 1.1 for more details). It can be used to debug common issues
with the devices used by the robot, such as connectivity or misconﬁguration.
This introduction gives a brief motivation for this bachelor thesis in section 1.1.
Since the Wolfgang robot platform is used for the RoboCup competition, it is
explained in section 1.2. Section 1.3 deﬁnes the goals of the thesis.
Chapter 2 presents related work in robot interface design, focusing on robots de-
signed for frequent interaction with humans. After that, chapter 3 explains some
basics as well as the bus and protocol used by the implementation. Next, chapter
4 describes the actual implementation and rationale behind important design de-
cisions. Chapter 5 then provides a short overview of the usability of the ﬁnished
work and relevant benchmarks while chapter 6 discusses these results. Finally,
Chapter 7 summarizes the ﬁndings and lists possible improvements to the current
implementation.

1.1 Motivation

The work done in this thesis is primarily intended for use with the Wolfgang
robot platform used by the RoboCup team Hamburg Bit-Bots. It consists of var-
ious devices [bit19] that communicate using the ROBOTIS Dynamixel Protocol
2.0 [ROBe] over an RS-485 or TTL bus.
Without a computer connected to the robot, it is not possible to monitor the status
of the connected devices. Devices may be unreachable for diﬀerent reasons:

• the device is physically disconnected

• the device is powered oﬀ or otherwise malfunctioning

1

1 Introduction

• the device’s packets are lost, either due to interference or a misbehaving bus

participant

• the device never sends any packet because it is waiting for another device

that is not sending for one of the reasons above

Figure 1.1: The Wolfgang robot platform

While it is always possible to connect a computer in case of an obvious malfunction,
this is a signiﬁcant amount of overhead. It does not allow for quick detection of
disconnected devices or anomalous readings of a single device. In a competition
like RoboCup, it is important to quickly detect problems in order to ﬁx them in
the ﬁeld. Noncritical errors may not disable the robot but they can still have an
impact on its performance in a game.
Due to the extensible nature of the protocol, other robot platforms using the same
protocol and a bus compatible with a UART (Universal Asynchronous Receiver
Transmitter) interface would also work, with code changes only required for adding
support for new device models.

1.2 RoboCup

RoboCup (https://www.robocup.org/) is a competition designed to promote
robotics and AI research. It intends to set challenges that are both technically

2

diﬃcult and socially impactful. The long term goal is to create fully autonomous
robots that can play soccer and win against the current winners of the FIFA World
Cup championship [robb].

1.2 RoboCup

Figure 1.2: A RoboCup soccer game

While soccer was the original idea behind RoboCup [roba], there are now many
diﬀerent categories that focus on speciﬁc challenges:

• RoboCupSoccer

• RoboCupRescue

• RoboCup@Home

• RoboCupIndustrial

• RoboCupJunior

The leagues in each category are based on the physical layout of the robot or
the speciﬁc task. For example, the RoboCupSoccer category [robd] includes the
following leagues:

• Humanoid

• Standard Platform

• Middle Size

• Small Size

• Simulation

3

1 Introduction

The Hamburg Bit-Bots team competes in the Humanoid league (KidSize and Teen-
Size) with robots built on the Wolfgang robot platform [robc].
By deﬁning clear rules and goals, the various RoboCup leagues make it possible to
compare and evaluate diﬀerent approaches in both robotics and AI research. They
also make research in these areas more visible to the general public.

1.3 Thesis Goal

The goal of this thesis is to determine a suitable microcontroller board and develop
the required ﬁrmware for

• collecting status information of the connected devices by passively listening

on the bus . . .

• displaying this information on an integrated touchscreen display and . . .

• navigating between detailed views for each device/model using the touch-

screen.

In particular, it should be possible to identify unreachable or disconnected devices
at a glance. Adding support for new device models should be easy and eﬀortless.
Both display and microcontroller should be compact enough to be able to attach
and detach them from a robot quickly.

4

2 Related Work

None of the qualiﬁed teams for the RoboCup Humanoid League 2019 had a ded-
icated display installed on their robots [robc]. Outside of research contests like
RoboCup and industrial applications, user interactions with robots are still rare.

Relatively common robots for domestic use are automatic vacuum cleaners and
lawnmowers. These robots usually feature only simple displays. Controls are
limited to buttons. Complex conﬁguration and maintenance for most models can
be performed using a separate application that has to be installed on the user’s
phone. Examples include the Roomba and Braava product lines by iRobot [iro].
The Pepper robot by SoftBank Robotics is a humanoid robot that focuses on social
interactions in human-centered environments like stores, schools or homes. It is
one of the few social robots that has seen limited success outside of research. In
addition to speakers and LEDs, it also features a large touchscreen on the chest.
The touchscreen is intended for interaction but can also be used for debugging
during development [PG18].

Figure 2.1: The Pepper robot1

1 Source: https://www.softbankrobotics.com/emea/themes/custom/softbank/images/

full-pepper.png (Accessed: 2020-03-30)

5

2 Related Work

Since the Pepper robot is highly customizable through software, it can be adapted
for a wide variety of scenarios. However, the lack of powerful or accurate
arms limits it to mostly informational roles.
It is used as the platform for the
RoboCup@Home Social Standard Platform League [PG18].
Similarly, the Human Support Robot by Toyota is used for the RoboCup@Home
Domestic Standard Platform League. As the name suggests, these robots are sup-
posed to assist humans in domestic contexts and are not optimized for complex
social interactions. They feature a simple display for showing additional informa-
tion [YTO+19].
Many teams in the RoboCup@Home Open Platform League 2019 also used various
types of displays for interfacing with their robots:

• The CATIE Robotics team uses modiﬁed PAL Robotics TIAGo robots. The
TIAGo is equipped with a laptop tray that was customized to make it ad-
justable. An Android tablet was mounted to the back of the head to serve
as a touch-capable input device [FAD+19].

• The homer@UniKoblenz team also uses a TIAGo as well as a custom robot-
based on the CU-2WD-Center robot platform. It has a small head-mounted
display that displays a face [MMW+19].

• The RoboFEI@Home team uses a custom robot with an enclosure for an Ap-
ple iPad 2 ” tablet. The tablet is primarily used to display a face [PMM+19].

• The RT Lions team use a screen and a mini-beamer that projects images on

a plastic dome to display the faces for their two robots [RWT+19].

6

3 Basics

This chapter explains some of the technologies used by the implementation. Sec-
tion 3.1 and section 3.2 describe the bus and protocol used by the Wolfgang robot
platform. Section 3.3 gives a brief overview of embedded operating systems. The
implementation uses an embedded OS to meet its latency requirements.

3.1 RS-485

RS-485 is a commonly used name for the ANSI TIA/EIA-485 standard.
It is
a speciﬁcation for a half-duplex serial bus. Data is transmitted over two wires,
usually labeled A and B, with a positive voltage on A and a negative voltage on B.
The voltage diﬀerence between these two wires determines the actual logic level.
A voltage diﬀerence less than or equal to −200 mV is a logical 0, while a diﬀerence
greater than or equal to 200 mV is a logical 1 [SZC02].
This two-wire setup makes the bus more resilient towards noise, allowing for op-
eration in noisy environments or over long distances.
For the purpose of this thesis, the only interesting fact is the diﬀerential trans-
mission. It requires an additional transceiver that converts the two signals into a
single signal at the microcontroller’s logic level. Such a signal can then easily be
consumed by a UART.

3.2 ROBOTIS Dynamixel Protocol 2.0

The ROBOTIS Dynamixel Protocol is a packet-based master/slave protocol used
by all of ROBOTIS’s products. This section describes only the improved version
2.0. Oﬃcial documentation can be found at ROBOTIS’s website [ROBe].
Each device is assigned a unique 8-bit ID that is used to determine the sender or
receiver of packets. IDs must be conﬁgured before connecting a device to the bus.
The user must make sure that IDs do not overlap. The IDs 0xff and 0xfd are not
allowed and 0xfe is reserved for broadcasts.
Once connected, the master (usually a powerful computer controlling the various
devices) can send an instruction packet. Instruction packets can target one or more
devices (for details see 3.2.1). Only devices targeted by an instruction are allowed
to write a status packet to the bus. If an instruction targets more than one device,
the responses are ordered by their ID. Due to this, no external synchronization for

7

3 Basics

the bus is required. Since instruction or status packets may be lost, the master
has to resend instruction packets if no packets have been received after a certain
amount of time.
Devices are seen as linear byte-addressed memory with 16-bit addresses (referred
to as control tables by the oﬃcial documentation). Usually, these are memory-
mapped registers that can be used to read or change the state of a device. However,
due to this simple view of a device as some amount of memory, the protocol can
be easily extended or reused by custom devices.

(a) Generic layout of an instruction packet

(b) Generic layout of a status packet

Figure 3.1: Generic packet layout

Each packet has some metadata preceding the actual payload. It starts with a
ﬁxed byte sequence that allows detecting a packet start without knowing where
the last packet ended.
It is followed by the device ID. For instruction packets,
this is the device that is targeted, for status packets it is the device that sent the
packet. The Length ﬁeld determines the remaining length of the packet. This
allows for a payload of variable size, depending on the instruction used or the data
returned by the status packet. The next ﬁeld is the instruction; status packets
use a reserved instruction. While the exact content of the payload varies, status
packets always store an additional error ﬁeld as the ﬁrst byte. This ﬁeld can be
used to indicate any errors that occurred during the processing of an instruction.
Since the payload can contain arbitrary values, it can also contain the byte se-
quence used to mark the start of a new packet. To prevent a receiver from misinter-
preting this byte sequence, byte stuﬃng is used. Whenever a payload contains the

8

3.2 ROBOTIS Dynamixel Protocol 2.0

byte sequence 0xff 0xff 0xfd, it is replaced by 0xff 0xff 0xfd 0xfd. This makes
it impossible to send a payload that could be interpreted as the start of a new
packet. The receiver simply removes the extra byte that was added. Note that
the Length ﬁeld speciﬁes the number of bytes with byte stuﬃng already applied.
The last two bytes of every packet contain the CRC-16/BUYPASS [Coo] checksum
of every byte in the packet, including the starting sequence (and excluding the
CRC itself). This checksum can be used to detect transmission errors, in case the
underlying bus does not have error detection built-in (RS-485 does not).

3.2.1 Instructions

Ping (0x01) Tests whether a device is connected. If the device ID is broadcast
(0xfe), all devices respond. The status packet contains the device’s model number
and ﬁrmware version.

Figure 3.2: Ping instruction payloads

Read (0x02) Reads bytes from the control table of a device. The status packet
contains the requested bytes.

Figure 3.3: Read instruction payloads

Write (0x03) Writes bytes to the control table of a device. The status packet
indicates whether the write was executed successfully and contains no additional
payload. Many devices can be conﬁgured to not send any status packets on writes.

9

3 Basics

Figure 3.4: Write instruction payloads

Reg Write (0x04)
Action instruction is received.

Identical to Write, except that the write is delayed until an

Figure 3.5: Reg Write instruction payloads

Action (0x05) Executes the write registered by the previous Reg Write instruc-
tion. The status packet indicates whether the write was executed successfully and
contains no additional payload. Many devices can be conﬁgured to not send any
status packets on writes.

Figure 3.6: Action instruction payloads

Factory Reset (0x06) Resets the device’s control table ﬁelds to their default
values. Reset Mode determines the values that are reset:

10

3.2 ROBOTIS Dynamixel Protocol 2.0

• 0xff: resets all values

• 0x01: resets all values except for the ID

• 0x02: resets all values except for the ID and the baud rate

The status packet indicates whether the reset was executed successfully and con-
tains no additional payload.

Figure 3.7: Factory Reset instruction payloads

Reboot (0x08) Reboots the device. The status packet indicates whether the
reboot was successful and contains no additional payload.

Figure 3.8: Reboot instruction payloads

Clear (0x10) Resets the multi-turn information of the device. This instruction is
very closely tied to servos and generally not useful for other kinds of devices.

Figure 3.9: Clear instruction payloads

11

3 Basics

Sync Read (0x82) Reads bytes from the control tables of multiple devices at
once. The device ID of the instruction packet must be broadcast (0xfe). The
status packet of each device contains the requested bytes. Devices respond in the
same order as their IDs in the instruction packet payload.

Figure 3.10: Sync Read instruction payloads

12

3.2 ROBOTIS Dynamixel Protocol 2.0

Sync Write (0x83) Writes bytes to the control tables of multiple devices at once.
The data for each device can be diﬀerent. The device ID of the instruction packet
must be broadcast (0xfe). The status packet of each device indicates whether
the write was executed successfully and contains no additional payload. Devices
respond in the same order as their IDs in the instruction packet payload. Many
devices can be conﬁgured to not send any status packets on writes.

Figure 3.11: Sync Write instruction payloads

13

3 Basics

Bulk Read (0x92) Reads bytes from the control tables of multiple devices at once.
Unlike Sync Read, this instruction allows for diﬀerent addresses and lengths for
each device. The device ID of the instruction packet must be broadcast (0xfe).
The status packet of each device contains the requested bytes. Devices respond in
the same order as their IDs in the instruction packet payload.

Figure 3.12: Bulk Read instruction payloads

14

3.2 ROBOTIS Dynamixel Protocol 2.0

Bulk Write (0x93) Writes bytes to the control tables of multiple devices at once.
Unlike Sync Write, this instruction allows not only for diﬀerent data but also for
diﬀerent addresses and lengths for each device. The device ID of the instruc-
tion packet must be broadcast (0xfe). The status packet of each device indicates
whether the write was executed successfully and contains no additional payload.
Devices respond in the same order as their IDs in the instruction packet payload.
Many devices can be conﬁgured to not send any status packets on writes.

Figure 3.13: Bulk Write instruction payloads

3.2.2 Byte-Order

All multi-byte values (packet ﬁelds, values in packet payloads and control table
ﬁelds) are little-endian. That is, for multi-byte values, the least signiﬁcant byte
comes ﬁrst, then the second least signiﬁcant byte, etc.

15

3 Basics

3.3 Embedded Operating Systems

Embedded operating systems are libraries linked directly with the user’s code.
They are small both in runtime overhead and in program size, making them ideal
for microcontrollers that cannot run full operating systems like Linux or Win-
dows. Embedded OSs only provide a small subset of the many features oﬀered by
traditional operating systems. Common features are:

• threads (sometimes also called tasks)

• concurrency primitives (mutexes, semaphores, queues, etc)

• memory allocators

• ﬁlesystems

The most signiﬁcant diﬀerence to traditional operating systems is the lack of se-
curity. Since the operating system is part of the program itself, all code can be
trusted and process boundaries are not needed [TB14].
The core of an embedded OS are threads and context switching. Being part of the
user program, the application must conﬁgure an interrupt that calls the scheduler,
which in turn runs application code in one of the threads. Threads can run on
separate CPU cores but they are also useful for single-core systems. Threads are
preemptive: one thread can be paused and another one started instead. This
makes it possible to guarantee that some threads always get the CPU time they
need, for example to process incoming data [freb].
The concurrent nature of threads makes it necessary to synchronize access to
shared data. Since synchronization is deeply intertwined with the scheduler, con-
currency primitives must also be provided by the embedded OS.

16

4 Implementation

This chapter describes the hardware the implementation uses (section 4.1) and
the developed ﬁrmware (section 4.2). The source code for the ﬁrmware can
be found at https://github.com/Laegluin/embedded_debug_interface_for_
robots/tree/thesis-ref. The version referenced by this thesis is tagged as
thesis-ref. The description of the ﬁrmware is intended to give a high-level overview
and discusses tradeoﬀs as well as points of interest.
Since the implementation targets the Wolfgang robot platform, it must be com-
patible with its RS-485 bus running at a speed of 2 MBd.

4.1 Hardware

The following hardware is used:

• STM32F7508-DK development board1

• MAX485 RS-485/RS-422 transceiver2

• FT232R USB to UART converter (for testing)3

The MAX485 transceiver is used to connect the RS-485 bus to the STM32F7508-
DK board. It outputs a 5 V signal that can be interpreted by one of the board’s
UARTs. STM32F7508-DK is built around an STM32F750N8H6 Arm Cortex-M7
based microcontroller. The controller’s UART6 is used, as it is easily accessible
through the board’s Arduino Uno compatible connectors at the back. All UARTs
have a theoretical maximum speed of 27 MBd [STM18c] (depending on the clock
conﬁguration), making the MAX485’s maximum speed of 2.5 MBd the maximum
speed of this setup [Max14][STM18d].
The STM32F7508-DK board has a built-in 4.3 ” 480x272 LCD-TFT capacitive
touchscreen. It is used to display and interact with the UI. Because it is built-in,
no further assembly is required [STM18d].
The STM32F750N8H6 microcontroller is based on an Arm Cortex-M7 CPU. It
supports clock speeds of up to 216 MHz and has both data and instruction caches.

1https://www.st.com/resource/en/user_manual/dm00537062-discovery-kit-for-

stm32f7-series-with-stm32f750n8-mcu-stmicroelectronics.pdf
2https://datasheets.maximintegrated.com/en/ds/MAX1487-MAX491.pdf
3https://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232R.pdf

17

4 Implementation

It is equipped with a single-precision FPU (ﬂoating-point unit) and a DMA con-
troller [STM18a]. While this is quite a lot of processing power for a microcontroller,
it is needed to drive an interactive UI while at the same time processing incom-
ing data quickly enough. The DMA controller allows transferring data from the
UART to memory at high data rates without using up CPU time.

Figure 4.1: The STM32F7508-DK development board4

The controller itself comes with only 64 KiB of embedded ﬂash memory. However,
it also has a Quad-SPI memory interface that can be used with external ﬂash
memory [STM18a]. The STM32F7508-DK board has 16 MiB of pre-installed ﬂash
memory [STM18d].
Similarly, 320 KiB of RAM are embedded in the controller [STM18a]. This is
more than enough for most applications but not enough for the video RAM
(VRAM) used by the display. When using double buﬀering and 8 bits per pixel,
at least 480 · 272 · 3 · 2 = 765 KiB are needed for VRAM alone. VRAM can
be located in external RAM which can be controlled by the microcontroller’s
FMC (ﬂexible memory controller). The board has 8 MiB of pre-installed exter-
nal RAM [STM18a][STM18d].

4 Source: https://www.st.com/bin/ecommerce/api/image.PF267270.en.feature-
description-include-personalized-no-cpn-large.jpg (Accessed: 2020-03-30)

18

4.2 Software

The STM32F7508-DK board is equipped with an ST-LINK/V2-1 in-circuit de-
It can be used for debugging and for programming the internal ﬂash
bugger.
memory [STM18d]. External ﬂash cannot be programmed using the ST-LINK;
instead, a standalone bootloader must be used (see subsection 4.2.1).
The FT232R USB to UART converter is only used for testing and benchmarking.
It can easily be connected to UART6 instead of the MAX485. Data can then be
sent to the USB serial port emulated by the FT232R from the computer connected
to it [Fut]. This makes testing extremely easy since the device can be treated as a
serial terminal.

4.2 Software

This section describes the ﬁrmware for the STM32F7508-DK board. The boot-
loader is written in C (C99), the actual ﬁrmware itself is written in C++ (C++14).
All code is compiled with the GNU arm-none-eabi toolchain. Newlib is used as
the C standard library implementation.

4.2.1 Bootloader

When the microcontroller is reset, it loads the vector table from address 0x00000000.
The vector table contains the addresses of all possible interrupt handlers. In ad-
dition, the ﬁrst item is the initial value of the stack pointer and the second is the
address of the entry point. After loading the vector table, the stack pointer is set
to the conﬁgured value and the processor jumps to the entry point [STM18c]. By
default, addresses in the range [0x00000000, 0x08000000) are mapped to 0x08000000,
which in turn is mapped to internal ﬂash memory [STM18c].
This poses a problem for applications that do not ﬁt into internal ﬂash memory:
there is no way to boot from the much larger Quad-SPI ﬂash memory or to program
it. An additional bootloader has to be used instead. A bootloader is a minimal
application that initializes a peripheral device for I/O, accepts commands as well
as data from said device and allows programming and booting from otherwise
unsupported memory.
In this case, the bootloader must allow programming and booting from Quad-
SPI ﬂash memory. It uses one of the STM32F7508-DK board’s micro-USB ports
for I/O [STM18d]. USB is a well-suited interface because data integrity checks
are built-in [usb00]. STMicroelectronics provides a USB 2.0 compliant library for
applicable microcontrollers that the bootloader uses for USB support [STM19a].
When the bootloader starts, it initializes the USB controller and the Quad-SPI
memory interface. It also blinks the board’s LED at regular intervals to indicate
that it is running. It then listens on the USB interface as a communication class
device.

19

4 Implementation

(a) ﬂash packet layout

(b) start packet layout

Figure 4.2: Bootloader packet layout

The bytes received are interpreted according to a custom, packet-based protocol.
The packet layout can be seen in ﬁgure 4.2. Packets start with a start sequence
that makes it possible to identify the beginning of a packet even if it is preceded by
unrelated bytes. To prevent unwanted start sequences in the packet itself, all bytes
following the start sequence must be escaped by adding byte stuﬃng: whenever a
byte that is not 0xff is followed by a 0xff byte, another 0xff byte must be added.
For example, the bytes 0x00 0xff 0xff must be sent as 0x00 0xff 0xff 0xff. The
bootloader simply removes the added bytes before processing the rest. Values of
more than one byte are encoded as little-endian and lengths are always given as
the length before any byte stuﬃng was applied.
A ﬂash packet instructs the bootloader to erase and then program the Quad-SPI
ﬂash memory with all the bytes in the Image ﬁeld, beginning at the start address
of the Quad-SPI ﬂash memory.
The start packet instructs the bootloader to start an application previously ﬂashed.
It disables all (pending) interrupts, exits interrupt handler mode if necessary and
enables the memory-mapped mode for the Quad-SPI memory interface. In addi-
tion, it also enables the board’s LED permanently, indicating that the application
is now running. Finally, it starts the application by loading the stack pointer
and jumping to the entry point in the same way the microcontroller does when
it boots from internal ﬂash memory. The bootloader assumes that the appli-
cation’s vector table starts at the beginning of the Quad-SPI ﬂash memory space
(0x90000000 [STM18c]). The application can also be started by pressing the board’s
programmable button (next to the reset button). The procedure is identical to
the one described above.

20

4.2 Software

Figure 4.3: After reset, the microcontroller starts the program in internal ﬂash
memory (the bootloader).
It then waits for packets to arrive over
USB. If a start packet has been received or the button was pressed, it
starts the application in Quad-SPI ﬂash memory.

The bootloader only has to be ﬂashed to internal ﬂash memory once. Afterward, it
can be used to program the Quad-SPI ﬂash memory and start an application from
it using the board’s micro-USB port. In this case, the application is the actual
ﬁrmware that controls the UI and processes packets sent over the Wolfgang robot
platform’s RS-485 bus.

4.2.2 Used Libraries

The following software libraries were used to aid the development of the ﬁrmware:

• STM32F7 HAL and Low-layer drivers5 (part of STM32CubeF7 1.15.0)

• STM32F7508-Discovery board support package6 (part of STM32CubeF7

5https://www.st.com/resource/en/user_manual/dm00189702-description-of-stm32f7-

hal-and-lowlayer-drivers-stmicroelectronics.pdf

6https://github.com/STMicroelectronics/STM32CubeF7/tree/master/Drivers/BSP/

STM32F7508-Discovery

21

start program from internal ﬂashresetbootloaderinitializationﬂash packet receivedstart packet receivedwait forpacketsprogram Quad-SPIﬂash memorybutton pressedstart application4 Implementation

1.15.0)

• STemWin version 5.44 (part of STM32CubeF7 1.15.0)

• FreeRTOS7 version 10.0.1 (part of STM32CubeF7 1.15.0)

• Catch28 version 2.10.2

The STM32F7 HAL and Low-layer drivers are various independent drivers for
peripherals found on hardware produced by STMicroelectronics. Despite the name
(HAL - hardware abstraction layer) they still require the user to write hardware-
speciﬁc code. They do oﬀer simpliﬁed interfaces that do not require manipulation
of memory-mapped peripheral device registers. For more complicated peripherals
like the LCD controller this can be helpful [STM17].
Similarly, the STM32F7508-Discovery board support package oﬀers drivers based
on the HAL and Low-layer drivers that are customized for the STM32F7508-DK
board. They encapsulate all of the hardware and have easier to use interfaces than
their HAL counterparts [STM19b].
STemWin is a GUI library based on emWin by SEGGER Microcontroller GmbH
& Co. KG. It is eﬀectively a precompiled version of emWin with driver sup-
port for STMicroelectronics’ hardware. While emWin is commercially licensed,
STemWin is licensed as free of charge for use with STMicroelectronics’ prod-
ucts
[STM19b][STM18b][SEG17]. Since it is otherwise indistinguishable from
emWin, it will be referred to as emWin in the following. emWin was chosen in-
stead of TouchGFX (also part of STM32CubeF7) because it does not require code
generation and has extensive documentation.
FreeRTOS is a popular embedded operating system. It is permissively licensed and
widely used by major companies. It is speciﬁcally designed to run with minimal
overhead (both code size and execution speed) [fred]. STMicroelectronics provides
a distribution of FreeRTOS that is already conﬁgured for their microcontrollers as
part of STM32CubeF7 [STM19b].
Catch2 is a unit testing library for C++11 and above. Tests are written as simple
functions with assertions and do not require complex setup. It is a header-only
library, meaning that no additional build system conﬁguration is necessary [cat].

4.2.3 Testing

Automatic testing of the hardware-speciﬁc code and the UI is diﬃcult. Tests
concerning the bus were done using the FT232R USB to UART converter to send

7https://www.freertos.org/
8https://github.com/catchorg/Catch2

22

4.2 Software

test data as well as traces of real bus traﬃc directly to the microcontroller’s UART.
UI tests were also performed manually, usually as part of the aforementioned tests.
Most of the core logic deals with data received over the bus. The actual origin of
the data is not relevant for testing. This code is carefully structured to avoid any
dependencies on hardware-speciﬁc code. It is tested using Catch2 unit tests run-
ning on the host platform (Linux on AMD64). While this is not a perfect solution
as there are still diﬀerences between the platforms like pointer sizes, alignment re-
quirements or hardware protection mechanisms provided by the operating system,
it creates high conﬁdence in the correctness of the code nevertheless.
In addition, manual tests on a real robot were also performed whenever possible.
Due to the high setup time these tests were intended as a ﬁnal quality measure
and not as a general tool for ﬁnding bugs.

4.2.4 Overview

On startup, the ﬁrmware ﬁrst conﬁgures the required peripheral devices. This
includes the UART (speciﬁcally UART6 ), the LCD controller and the external
RAM used as a frame buﬀer for emWin. Care must be taken when using the
external RAM in combination with another device (the LCD controller in this case)
as external RAM is cached by the CPU. Since the LCD controller does not know
about any CPU caches, writes to the frame buﬀers will not be visible to it until
the writes are ﬂushed to memory, causing visible artifacts on the screen [STM18c].
This can be prevented by using the microcontroller’s MPU (memory protec-
tion unit). The MPU allows disabling write caching for certain memory re-
gions [STM18c]. Reads can still be cached since only the CPU writes to the
frame buﬀer. Additionally, the MPU is also used to disable access to a 4 KiB
region starting at 0x00000000. This helps catch dereferences of null -pointers—a
common programming error—early. Otherwise, null -pointer dereferences would
be perfectly valid, since the address 0x00000000 is mapped to the start of the in-
ternal ﬂash memory (see subsection 4.2.1).
Finally, the FreeRTOS scheduler has to be started. It takes over the execution and
starts scheduling tasks (FreeRTOS uses this term instead of thread). The SysTick,
SVCall, and PendSV interrupts must use the handlers provided by FreeRTOS in
order for FreeRTOS to function correctly. The SysTick interrupt must also run at
the lowest possible interrupt priority [frec]. This conﬂicts with STMicroelectronics’
HAL library, which expects to be called from the SysTick interrupt running at
the highest priority [STM17]. As a workaround, the HAL library is called from
a separate timer interrupt that is running at the highest priority and identical
frequency to the SysTick interrupt.
Since tasks scheduled by FreeRTOS run concurrently, it is necessary to secure
any shared state against concurrent accesses. This also applies to Newlib, the C

23

4 Implementation

standard library implementation that is used. Its malloc implementation is used
for all heap allocations in the standard library, including C++ containers like
std::vector, but is not safe to use concurrently [new]. There are ways to secure
it by providing a global lock; however, FreeRTOS already includes an optimized
concurrency safe memory allocator [frea]. The linker’s --wrap option [Fre16] is used
to replace the malloc function with a custom implementation that simply calls the
FreeRTOS allocator. This way all code automatically uses the correct allocator.
There are two tasks that have to run concurrently: one is processing incoming data
and the other is updating the UI. Both of these tasks share two data structures that
are each protected by a mutex. The Log object stores recent errors and proﬁling
information whereas the ControlTableMap stores all currently known information
about devices connected to the RS-485 bus (for more detail see 4.2.6).
The packet processing task runs at a higher priority than the UI task. This means
it will run until it deliberately yields control to lower priority tasks for a short
amount of time. This way the UI task only gets a limited amount of processing
time, leaving the rest for packet processing. If the UI task is currently holding the
lock on a mutex and the packet processing task is trying to lock the same mutex,
the FreeRTOS scheduler temporarily assigns the priority of the packet processing
task to the UI task (priority inheritance). The UI task can now run until it releases
the lock, at which point it reverts to its previous priority and is preempted by the
packet processing task [free]. Again, the UI task only runs as long as it has to,
freeing the rest of the time for packet processing.
The following two subsections describe the design of the two tasks in more detail.
Subsection 4.2.5 describes the UI task, subsection 4.2.6 the packet processing task.

4.2.5 UI Task

The UI task is responsible for updating and drawing the UI as well as processing
touch input. The task simply consists of an inﬁnite loop calling the emWin func-
tion GUI_Exec, which handles user input and timers. A separate hardware timer
interrupt polls the touch controller at 30 Hz and stores updates to its state in
emWin’s input queue.

Listing 4.1: Main loop of the UI task

1
2
3

while ( true ) {

GUI_Exec () ;

}

In emWin, every part of the user interface is a window: windows themselves,
buttons, scrollbars, lists, etc. Every window is identiﬁed by a handle. A handle
is an integer that emWin associates with a window. All functions operating on a

24

4.2 Software

window take its handle as an argument. Some of these functions only apply to some
types of windows, like for example functions for manipulating buttons [SEG17].
Every window also has a callback function associated with it. This function is
called whenever the window receives a message. Messages can be user input,
elapsed timers, notiﬁcations from other windows or even a request to draw itself.
Callbacks can be overridden by supplying a new function to use instead. Often,
this function only handles some messages and delegates the remaining messages
to the original callback function. Most importantly, callbacks are a way to react
to user input on a speciﬁc window [SEG17].
The goal of the UI is to make it easy to identify the status of devices at a glance.
It is split into three separate views, each displaying information at a diﬀerent level
of detail: the device overview, the model overview, and the device details view.
A fourth view displays proﬁling information and log messages. Every view is a
distinct window that covers the entire screen. Color coding is used to diﬀerentiate
between connected and disconnected devices. Every list item or button represent-
ing a connected device is colored green, those representing disconnected devices
are colored red. The following four paragraphs give a brief overview of each view.

25

4 Implementation

Device overview Displays the total number of devices and the number of devices
for each model. It is the view shown when the application is started and is meant
to give a brief summary of all devices. Each summary for a certain model can be
clicked to open the model overview of that model. It also features buttons to reach
the device details view and the log view. While this view does not provide much
detail, disconnected devices are immediately visible. It is updated every 500 ms.

Figure 4.4: Screenshot of the device overview. The top bar is red because at least
one device (two in this case) is disconnected. The squares below the
bar show the status of the devices of a speciﬁc model. They also turn
red if at least one device is disconnected. The list containing them is
horizontally scrollable. Each square can be clicked and will open the
model overview for the corresponding model.

26

4.2 Software

Model overview Displays the status and ID of each device of a certain model.
Each device in the list can be clicked to open the device details view and select
that device. This view does not provide as much detail as the device details view
but it only shows devices of one particular model, making it easy to ﬁnd the exact
device that is disconnected. It is updated every 500 ms.

Figure 4.5: Screenshot of the model overview. The top bar is red because at least
one device for the selected model (MX-106) is disconnected. Below the
bar is a scrollable list with an item for each device of the selected model.
The device’s ID is shown in parentheses and the item is colored red
when it is disconnected. Clicking an item will navigate to the device
details view and select the clicked device.

27

4 Implementation

Device details view Displays all known values of a single device’s control table.
Diﬀerent devices can be selected by using the list on the left-hand side. This
view provides the maximum amount of detail per device but makes it harder to
determine the status of all connected devices at once. It is updated every 500 ms.

Figure 4.6: Screenshot of the device details view. The list on the left-hand side
contains an item for each connected device that is colored green when
the device is connected and red otherwise. Clicking an item will select
that device and show all values of its control table in the table on the
right-hand side.

28

4.2 Software

Log view Displays proﬁling information such as free memory and maximum and
average processing times, as well as the last 50 errors that occurred during packet
processing. This view is mostly intended for debugging. It has to be refreshed
manually since a lot of errors may occur in short bursts, making it impossible to
actually read an individual error message.

Figure 4.7: Screenshot of the log view. The left-hand side contains proﬁling in-
formation like processing times and free memory, the right-hand side
shows the 50 most recent error messages. The timestamps in the er-
ror log are relative to the start of the application. The view is only
refreshed when the Refresh button is clicked.

All of the views have to regularly access data shared with the packet processing
task. While they are holding the lock for this data, the packet processing task
may be blocked on this lock. This makes it extremely important to minimize the
time spent holding any locks. All of the views do this by copying the needed data
before processing it. Thus, they only ever hold a lock to make copies, which is
relatively quick compared to updating the entire UI at the same time. This does
decrease the theoretical performance of the UI; however, the UI only needs to be
fast enough to not appear slow to the user. In comparison, the packet processing
task has strict deadlines. If it is blocked for too long, it will miss incoming data.

4.2.6 Packet Processing Task

The packet processing task is responsible for processing the data the UART con-
nected to the RS-485 bus receives. Since the bus has a data rate of 2 MBd,

29

4 Implementation

1
2
3
4
5
6
7
8
9
10
11

performance is crucial. Data must be processed faster than it arrives in order to
not lose any of it. At the same time, there needs to be enough processing time left
to also update to UI.
The code is designed to work with more than one bus at the same time. Each
bus is associated with a Connection object. It holds the state of the packet parser,
some proﬁling information and a pointer to a buﬀer that stores received data. At
the moment, only a single bus connected to UART6 is supported.

Listing 4.2: Main loop of the packet processing task

while ( true ) {

for ( auto & connection : connections ) {

if ( connection . la st_p roce ssing _sta rt == 0) {

connection . last _pro cess ing_s tart = HAL_GetTick () ;

}

process_buffer ( log , connection , control_table_map ) ;

}

vTaskDelay (4 / portTICK_PERIOD_MS ) ;

}

The buﬀer is automatically ﬁlled by the DMA controller. It transfers the bytes
from the UART’s receive register and raises interrupts when half of or the entire
buﬀer has been ﬁlled. Once it has been ﬁlled, the DMA controller starts at the
beginning of the buﬀer again. The interrupt handler sets a ﬂag that determines
which part of the buﬀer is now ready. As long as the data is processed faster than
it is received, no data will be lost. Even when the data is not processed quickly
enough, there will be no serious malfunctions. Some data may be corrupted but
this will usually be detected by the CRC checksums that are part of the ROBOTIS
Dynamixel protocol (see section 3.2).
The size of the buﬀer has a signiﬁcant impact on the maximum time allowed before
data is lost. A larger buﬀer increases this time but also increases the latency. The
latency can largely be ignored because it is still low (for human time scales) given
the possible buﬀer sizes. Latency would increase drastically if there were no or
only very little traﬃc on the bus, as data is only ever processed once one half of
the buﬀer is ready. Other than by memory constraints, the size of the buﬀer is
limited to 65 535 B by the size of the DMA controller’s NDT register [STM18c].
The buﬀer’s size is 8192 B. This means that even assuming the absolute worst case,
4096 B
2 MBd/8 ≈
the maximum amount of time for processing one half of the buﬀer is
16 ms. Realistically, the maximum amount of time will be higher for multiple
reasons:

• The baud rate of the bus is not equivalent to the bit rate of the incoming

data, since this equation ignores overhead like stop bits.

30

4.2 Software

• In practice, it is impossible to have 100 % load on the bus.

• The equation assumes that processing starts right after an interrupt signals
that one half of the buﬀer is ready, and does not actually process a single
byte. Normally, data is then being processed, which continuously moves the
point at which a collision with the DMA controller can occur.

For these reasons, if the maximum amount of time between processing one half of
the buﬀer never exceeds 16 ms, there will be no data loss or corruption.

Figure 4.8: After more than half of the DMA buﬀer has been ﬁlled, the front of
it is ready and can be read. At the same time, the back of it is now
invalid because the DMA controller is writing to it. The situation is
reversed when the DMA controller has ﬁnished writing to the back and
starts at the front again.

Since the buﬀer is written to by the DMA controller and then read by the CPU,
the CPU must not cache reads. This is accomplished by placing the buﬀer in
the DTCM RAM section of the microcontroller’s memory. DTCM RAM is never
cached [STM18c].
After processing one half of each buﬀer per bus, control is yielded to the UI task
for 4 ms. The UI can only be updated during this time. Increasing this time also
increases the responsiveness of the UI while increasing the time spent between the
processing of data.
The process_buffer function then parses packets until all the data in the
ready buﬀer has been consumed. Each successfully parsed packet is passed to
ControlTableMap::receive, which processes the contents of the packets. Errors and
proﬁling information are passed to the Log object afterward.
Due to this, the mutexes for the ControlTableMap and the Log object are never
locked at the same time. The UI task also never locks more than one of these
mutexes at a time. Holding only one lock at the same time prevents deadlocks.
The lock for the ControlTableMap object is intentionally held for almost the whole
duration of the call. Unlike with the UI task where holding the lock for a long time
would block the packet processing task, there is no task to block since the only

31

frontbackDMA controller positionfront ready,back invalidfront invalid,back ready4 Implementation

other task is the UI task which can only run when the packet processing explicitly
yields control. Maximizing the time holding a mutex removes the overhead of
locking it multiple times.

Parser The Parser is responsible for parsing packets from the ready part of a
It consumes bytes from a Cursor. A Cursor is essentially a pointer to a
buﬀer.
part of the buﬀer that also tracks how many bytes have already been read. This
enables a simple API for the Parser itself. Each call to the parse method either
parses one packet successfully, encounters an error or parses a packet partially. In
all cases, the Cursor tracks the current position and indicates when all bytes have
been consumed, while the Parser holds state that must be retained across parses.
Most importantly, it stores the previous three bytes. When inspecting the next
byte there are three possible scenarios:

• the byte and the previous three bytes are the header of a new packet

• the byte is stuﬃng (it can be ignored)

• the byte is a regular byte

In case the header of a packet is detected while already parsing a packet, an error
is returned. Returning early when encountering an error or only partially parsing
a packet is possible because the Parser stores the part of the packet currently being
parsed and the incremental CRC checksum.

Listing 4.3: Deﬁnition of the Packet struct

1
2
3
4
5
6

struct Packet {

DeviceId device_id ;
Instruction instruction ;
Error error ;
std :: vector < uint8_t > data ;

};

The speed of the Parser is critical to performance. To avoid allocating memory
while parsing, the parse method takes a pointer to a Packet struct as argument.
Since packets are processed sequentially, the same Packet struct can be reused.
Packets themselves can have diﬀerent lengths but when deﬁning a maximum al-
lowed packet length, the memory for a Packet of that length can be preallocated.
Deﬁning a maximum packet length also makes sense in order to avoid running out
of memory due to packets with incorrect Length ﬁelds.
The Packet struct represents both instruction and status packets since the only
diﬀerence between them is the addition of an Error ﬁeld for status packets (see
section 3.2). For instruction packets the error member can be ignored because it
will never contain an error.

32

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

4.2 Software

ControlTableMap The ControlTableMap object then processes these Packet structs
further. Status packets are left as is but instruction packets are parsed into
InstructionPacket structs. An InstructionPacket is a discriminated union of structs
for each instruction. Because the instruction speciﬁc ﬁelds are part of the pay-
load of a packet, parsing them is simple. Unlike the packet parser, the instruction
It also reuses previous InstructionPackets but
packet parser is just a function.
does allocate memory. Further optimization was not required to achieve the de-
sired performance.

Listing 4.4: Deﬁnition of the InstructionPacket struct

struct In structionPacket {

// constructors , destructor and member functions omitted

Instruction instruction ;
union {

PingArgs ping ;
ReadArgs read ;
WriteArgs write ;
RegWriteArgs reg_write ;
ActionArgs action ;
FactoryResetArgs factory_reset ;
RebootArgs reboot ;
ClearArgs clear ;
SyncReadArgs sync_read ;
SyncWriteArgs sync_write ;
BulkReadArgs bulk_read ;
BulkWriteArgs bulk_write ;

};

};

For every received instruction packet, the ControlTableMap records the devices that
are expected to respond. When a new instruction packet is received, a counter for
each device from which a status packet was not received is incremented. These
counters are reset when a status packet from the corresponding device has been
received. Devices that have not responded to more than four instruction packets
are considered disconnected.
Ping instructions are handled diﬀerently: the status packet responding to a Ping
instruction contains the model number of the device. The model number is used
to register a new device. Each device is mapped to a ControlTable object that
stores the current state of the device’s control table. If the device is not registered,
has a diﬀerent or an unknown model number, a new ControlTable matching the
model number is allocated. A device’s model can be unknown if status packets
from that device have been received without previously receiving the response to
a Ping instruction.
Whenever data is written to or read from a device, the written or read data is

33

4 Implementation

also updated for the ControlTable object belonging to that device. This is the data
that is displayed by the UI. Only the following instructions are handled properly:

• Ping

• Read

• Write

• Sync Read

• Sync Write

• Bulk Read

• Bulk Write

The remaining instructions are mostly ignored but still used for detecting discon-
nected devices. Adding support for them would be a signiﬁcant eﬀort especially
considering that these instructions do not appear in most traﬃc. The current im-
plementation also assumes that writes do not require a status packet response, as
that is how the Wolfgang robot platform is conﬁgured.
The ControlTable objects are identiﬁed by the ID of the device they belong to. Ini-
tially, a std::unordered_map was used but the performance proved to be insuﬃcient.
Instead, the objects are stored in a custom data structure. It takes advantage of
the fact that device IDs are only one byte and that ControlTable objects must
be accessed through a pointer (four bytes on a Cortex M7 processor [STM18c]).
The objects are simply stored in an array that is indexed by the device ID. An
additional boolean ﬂag indicates the presence or absence of the object. The entire
array only requires 256·(4+1+3) = 2048 B of memory (this includes three bytes of
padding). This solution trades memory and iteration speed for fast access times.
Since objects must be accessed for almost every received packet, this provides a
serious speedup compared to std::unordered_map.

ControlTable The control table of each device is represented by a ControlTable
object. For each device model, there is a diﬀerent subclass of ControlTable. Most
received packets update the ControlTable object of at least one device, performance
is thus an important design consideration. Adding or changing the ControlTable
of a device has to be easy.
The interface deﬁnition of the ControlTable base class can be seen in listing 4.5.
is_unknown_model determines if the model number is known and model_number re-
turns its value if present. set_firmware_version is called when the ﬁrmware version
is reported by the response to a Ping instruction. device_name simply returns a

34

4.2 Software

human-readable name of the model represented by the ControlTable. It is used for
display purposes only.

Listing 4.5: Deﬁnition of the ControlTable class

class ControlTable {

public :

virtual ~ ControlTable () = default ;

virtual std :: unique_ptr < ControlTable > clone () const = 0;

virtual bool is_unknown_model () const ;

virtual uint16_t model_number () const = 0;

virtual void set_firmware_version ( uint8_t version ) = 0;

virtual const char * device_name () const = 0;

virtual ControlTableMemory & memory () = 0;

virtual const ControlTableMemory & memory () const = 0;

virtual const std :: vector < ControlTableField >& fields () const =

0;

bool write ( uint16_t start_addr , const uint8_t * buf , uint16_t

len ) ;

std :: vector < std :: pair < const char * , std :: string > > fmt_fields ()

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

20
21

22
23

const ;

24

};

The core functionality of ControlTable class uses the memory and fields methods.
The ControlTableMemory object returned by a call to memory is responsible for storing
the actual data. It is made up of multiple Segments that each describe a region of
memory:

• data segments are some memory starting at a certain address

• indirect address segments allow redirecting addresses (required to support

ROBOTIS MX-64 and MX-106 servos)

• unknown segments allow no reads and ignore writes (these are used when

the model number is not known)

The descriptions are used by the ControlTableMemory object to map data contained
in packets to a single, ﬂat byte array. Calls to the write method of a ControlTable

35

4 Implementation

object are forwarded to the ControlTableMemory. By using an accessor, only one
virtual call has to be performed, even when writing more than one byte.
The fields method returns a description of all ﬁelds in a device’s control table.
Each ControlTableField stores the address, type, name, and default value of a
single ﬁeld. It also contains a function for formatting the value of the ﬁeld as a
human readable string.

Listing 4.6: Deﬁnition of the control table ﬁelds of a Rhoban DXL Board
const std :: vector < ControlTableField > Cor eBoar dCon trol Table :: FIELDS

{

ControlTableField :: new_uint16 (0 , " Model Number " ,

Co reBoa rdCo ntrol Tabl e :: MODEL_NUMBER , fmt_number ) ,
ControlTableField :: new_uint8 (2 , " Firmware Version " , 0 ,

fmt_number ) ,

ControlTableField :: new_uint16 (10 , " LED " , 0 , fmt_bool_on_off ) ,
ControlTableField :: new_uint16 (12 , " Power " , 0 , fmt_number ) ,
ControlTableField :: new_uint32 (14 , " RGB LED 1 " , 0 , fmt_core_rgb ) ,
ControlTableField :: new_uint32 (18 , " RGB LED 2 " , 0 , fmt_core_rgb ) ,
ControlTableField :: new_uint32 (22 , " RGB LED 3 " , 0 , fmt_core_rgb ) ,
ControlTableField :: new_uint16 (26 , " VBAT " , 0 , fmt_core_voltage ) ,
ControlTableField :: new_uint16 (28 , " VEXT " , 0 , fmt_core_voltage ) ,
ControlTableField :: new_uint16 (30 , " VCC " , 0 , fmt_core_voltage ) ,
ControlTableField :: new_uint16 (32 , " VDXL " , 0 , fmt_core_voltage ) ,
ControlTableField :: new_uint16 (34 , " Current " , 0 , fmt_core_current

) ,

ControlTableField :: new_uint16 (36 , " Power On " , 0 ,

1

2

3

4
5
6
7
8
9
10
11
12
13
14

15

fmt_core_power_on ) ,

16

};

These descriptions are used by the fmt_fields method. It reads the current value
of a ﬁeld from the ControlTableMemory and formats it using the formatting function.
This function is used to display the contents of a device’s control table. Formatting
all ﬁelds is quite slow, which is why the UI task ﬁrst copies the entire ControlTable
object using the clone method. It eﬀectively acts as a virtual copy constructor.
To add support for a new device model, one only has to create a new subclass of
ControlTable and construct an instance of it when a response to a Ping instruction
is received. Currently, the following device models are supported:

• ROBOTIS MX-64 servos (http://emanual.robotis.com/docs/en/dxl/

mx/mx-64-2/)

• ROBOTIS MX-106 servos (http://emanual.robotis.com/docs/en/dxl/

mx/mx-106-2/)

• Rhoban DXL Boards (https://github.com/Rhoban/DXLBoard)

36

4.2 Software

• BitFoot foot pressure sensors (https://github.com/bit-bots/bit_foot)

• Hamburg Bit-Bots IMU modules (https://github.com/bit-bots/imu_

module)

37

5 Evaluation

This chapter evaluates the performance of the implementation described in chapter
4. Two measurements were taken to assess the performance:

• The time required to process the ready half of the receive buﬀer (see sub-
section 4.2.6). This measurement will be called time per buﬀer in the
following.

• The time that passes between two calls of the process_buffer function (again,
see subsection 4.2.6). This measurement will be called time between
buﬀers in the following.

The time per buﬀer measures the performance of the part of the system that actu-
ally deals with incoming data. It does not measure idle time and synchronization
overhead. The time between buﬀers on the other hand measures the performance
of the entire system. It indicates how much time passes between two opportunities
to process incoming data. This means that if this time does not exceed the max-
imum amount of time of 16 ms calculated in subsection 4.2.6, no incoming data
will be lost.
In addition, the perceived responsiveness of the UI is also reported. These ob-
servations are entirely subjective and only meant to give an impression of the
responsiveness to be expected.
The source code of the ﬁrmware and scripts used for measurements as well as
the results can be found at https://github.com/Laegluin/embedded_debug_
interface_for_robots/tree/thesis-benchmark-ref. The version used for
measurements is tagged as thesis-benchmark-ref.
All code was compiled with GCC 6.3.1 with maximum optimizations, link-time
optimization and no exception support (-O3 -flto -fno-exceptions).
Section 5.1 describes the method used to obtain the measurements and section 5.2
presents the results.

5.1 Measurement Method

The FT232R USB to UART converter listed in section 4.1 was used to simulate
an actual RS-485 bus. Three diﬀerent kinds of simulated traﬃc were used:

• A trace of real traﬃc from the bus of a robot of the Hamburg Bit-Bots.

39

5 Evaluation

• Synthetic traﬃc of 20 devices consisting of Ping instructions followed by
Read, Write, Sync Read, Sync Write, Bulk Read and Bulk Write instructions
for each device, repeated 300 times.

• Synthetic traﬃc of 20 devices that are constantly responding to Ping in-
structions. Devices change their model number after each Ping instruction.

The simulated traﬃc was sent to the USB to UART converter in two ways:

• the entire ﬁle of simulated traﬃc at once

• one packet at a time, with 100 µs delay per packet

A python script was used to send the simulated traﬃc. Output buﬀering was
disabled. To minimize the system call overhead when not adding any delay, the
ﬁles containing the simulated traﬃc all had a size of at least 400 KiB. When the
ﬁle was smaller, it was made bigger by simply repeating the contents.
All combinations of the aforementioned parameters (for a total of six diﬀerent com-
binations) were tested as separate experiments. Before starting the experiments,
the microcontroller was reset and every view of the UI was opened at least once to
ensure that every view would be updated. Measurements were taken for at least
80 s after reset.
The ﬁrmware had to be modiﬁed slightly to allow for the collection of the measure-
ments. An additional timer was used to generate an interrupt every 0.1 ms. The
interrupt handler incremented a counter every time it was called. This counter
was used in calls to process_buffer to determine the current time. Thus, every
measurement has an accuracy of 0.1 ms.
Measurements were stored on external RAM. After enough measurements had
been taken, the microcontroller was halted using the debugger. The debugger was
then used to dump the memory that stored the measurements. The raw data was
converted to a JSON ﬁle and then plotted using two python scripts.
The interrupts generated by the additional timer and the extra code to store the
measurements on comparatively slow external RAM imposed overhead that is not
present during normal execution. As a consequence, all times measured are an
upper bound on the expected values. The diﬀerences should be minimal, however.

5.2 Results

This section presents the results of the experiments for each of the six combinations
mentioned above. Every experiment is presented in a separate subsection. There
are four diﬀerent plots for each experiment. The scatterplots show the time per
buﬀer and time between buﬀers over time. Since each data point represents a

40

5.2 Results

duration, points in the plots are placed at the geometric mean of the start- and
endpoint of the duration. The histograms show the distribution of durations for
each scatterplot.
Subsection 5.2.7 contains tables for maximum, median, mean and minimum time
per buﬀer and time between buﬀers for each experiment. It also shows the data
rates that can be derived from the results in an additional table.
The ﬁrst 20 s of measurements were discarded to allow for the manual setup, the
next 60 s were used to generate the following plots and tables.

41

5 Evaluation

5.2.1 Trace, no delay

(a) Scatterplot of time per buﬀer

(b) Histogram of time per buﬀer

(c) Scatterplot of time between buﬀers

(d) Histogram of time between buﬀers

Figure 5.1: Time per buﬀer and time between buﬀers for trace traﬃc with no delay

UI responsiveness The UI was responsive, there was regular but short stuttering.

Most of the measurements of time per buﬀer are clustered around 8–10 ms. There
are noticeable exceptions that occur at regular intervals. These are most likely
packets that were not transmitted correctly at the time the trace was recorded.
Because they were malformed, they were ignored after parsing, leading to less time

42

5.2 Results

spent processing the buﬀer that contained these errors. Transmission errors that
occurred during the measurements are unlikely to have had a signiﬁcant impact
due to the extremely short cable length. In addition, these errors would not appear
at regular intervals, while recorded errors would be repeated every time the trace is
repeated, which happened frequently since the size of the trace was only 516 KiB.
There are two distinct spikes in the time between buﬀers. The higher spike is
caused by those measurements that were taken while a buﬀer was being processed.
Most of the measurements are about 4 ms. These are the measurements taken
when there was no data to process. They are the majority, indicating that higher
data rates could be handled without a problem.
It is unclear why the time between buﬀers is so tightly clustered around certain
times. It is possible that these clusters were caused by synchronization with one of
the mutexes. Since the time the UI task was holding a lock was always the same
and since FreeRTOS could only preempt a task every millisecond, there was only
a very limited set of possible wait times for the packet processing task. These wait
times may have been what caused the tight clustering.

43

5 Evaluation

5.2.2 Trace, 100 µs delay

(a) Scatterplot of time per buﬀer

(b) Histogram of time per buﬀer

(c) Scatterplot of time between buﬀers

(d) Histogram of time between buﬀers

Figure 5.2: Time per buﬀer and time between buﬀers for trace traﬃc with 100 µs

delay

UI responsiveness The UI was responsive, there was only occasional minimal
stuttering.

All measurements look extremely similar to those in the experiment with no delay.
Since the additional delay reduced the eﬀective data rate (see table 5.3), there were

44

5.2 Results

fewer packets processed in the same time frame and the inﬂuence of malformed
packets was not as severe.
The time between buﬀers is absolutely dominated by measurements taken when
there was no data to process. This is not surprising, as even less time was spent
processing data when there was also a delay per packet.

45

5 Evaluation

5.2.3 Synthetic Read/Write instructions, no delay

(a) Scatterplot of time per buﬀer

(b) Histogram of time per buﬀer

(c) Scatterplot of time between buﬀers

(d) Histogram of time between buﬀers

Figure 5.3: Time per buﬀer and time between buﬀers for synthetic read/write traf-

ﬁc with no delay

UI responsiveness The UI was still usable but there was heavy stuttering. Using
the UI was not pleasant.

Compared to the experiments using the recorded trace, there are almost no outliers

46

5.2 Results

in the measurements. The synthetic nature of the data is clearly visible. Measure-
ments are extremely clustered and all clusters are very close to each other.
These clusters were most likely caused by the diﬀerent types of packets that are
part of the data. The same types of packets were always sent as a sequence. Every
type had a slightly diﬀerent length and took a slightly diﬀerent path through the
program. This did not make a signiﬁcant diﬀerence to the overall time but it was
enough to consistently change the time it took to process a buﬀer, depending on
the types of packets it contained.

47

5 Evaluation

5.2.4 Synthetic Read/Write instructions, 100 µs delay

(a) Scatterplot of time per buﬀer

(b) Histogram of time per buﬀer

(c) Scatterplot of time between buﬀers

(d) Histogram of time between buﬀers

Figure 5.4: Time per buﬀer and time between buﬀers for synthetic read/write traf-

ﬁc with 100 µs delay

UI responsiveness The UI was responsive, there was only occasional short stut-
tering.

Like the experiment using the recorded trace, results when adding a delay per
packet are very similar to those without delay. Again, clusters in the time per buﬀer

48

plots are less pronounced as there are less measurements and the measurements
for the time between buﬀers are dominated by constant overhead.

5.2 Results

49

5 Evaluation

5.2.5 Synthetic Ping instructions, no delay

(a) Scatterplot of time per buﬀer

(b) Histogram of time per buﬀer

(c) Scatterplot of time between buﬀers

(d) Histogram of time between buﬀers

Figure 5.5: Time per buﬀer and time between buﬀers for synthetic ping traﬃc with

no delay

UI responsiveness The UI was not responsive at all. While it was still possible
to use, scrolling did not work properly and any action caused signiﬁcant and
noticeable delays.

The results for the time per buﬀer are signiﬁcantly worse than in the previous

50

5.2 Results

experiments. The maximum time per buﬀer exceeds 50 ms and there are many
outliers. These outliers were most likely caused by errors during parsing: since the
buﬀers were not processed quickly enough, the DMA controller was overwriting
buﬀers as they were being read.
The time between buﬀers reﬂects the measurements for time per buﬀer. However,
it is notable that there are many measurements of only about 4 ms, even though
the processing was too slow. This is because after processing one buﬀer, there was
a high likelihood that the next buﬀer was not currently ready. Data was not lost
during these waits but during the processing itself, meaning that the number of
waits only decreased because more time was spent processing data.
Because so much time was spent processing data, the amount of time dedicated to
the UI decreased and the latency increased. The high latencies caused problems
with input handling since input could not be processed in time. Less time for the
UI task also meant the real-time required for rendering the UI increased.

51

5 Evaluation

5.2.6 Synthetic Ping instructions, 100 µs delay

(a) Scatterplot of time per buﬀer

(b) Histogram of time per buﬀer

(c) Scatterplot of time between buﬀers

(d) Histogram of time between buﬀers

Figure 5.6: Time per buﬀer and time between buﬀers for synthetic ping traﬃc with

100 µs delay

UI responsiveness The UI was mostly usable but there was signiﬁcant stuttering.
Scrolling mostly worked but was not pleasant to use. There were noticeable but
not signiﬁcant delays when interacting with buttons.

Results with delay per packet look remarkably similar to those for the experiments

52

5.2 Results

with synthetic Read and Write instructions. The only diﬀerence is that all times
increased drastically to about 57–59 ms. The reason is that while the average time
per buﬀer was still about four times higher than the allowed maximum of 16 ms,
the delay per packet slowed down the eﬀective data rate enough to make the actual
allowed maximum greater than the measured maximum time per buﬀer.
This can clearly be seen when comparing the eﬀective data rates in table 5.3: the
eﬀective data rates with added delay are all comparable, whereas the eﬀective data
rate for synthetic Ping instructions with no delay is signiﬁcantly lower than the
others.
It is also the reason the UI was so much more responsive than without any delay.
The problems caused by high latencies were still present but the UI task did have
enough time to render the UI at a suﬃcient speed.

53

5 Evaluation

5.2.7 Results by Experiment

Experiment Maximum Median Mean Minimum

Trace, no delay
Trace, 100 µs delay
Synthetic Read/Write
instructions, no delay
Synthetic Read/Write
instructions, 100 µs delay
Synthetic Ping instructions,
no delay
Synthetic Ping instructions,
100 µs delay

10.1 ms
9.4 ms
11.9 ms

8.8 ms
7.7 ms
11.2 ms

8.6 ms
7.6 ms
11.2 ms

0.9 ms
0.9 ms
10.6 ms

11.7 ms

10.9 ms

10.9 ms

10.3 ms

54.2 ms

52.7 ms

50.8 ms

37.0 ms

58.7 ms

57.9 ms

57.9 ms

57.0 ms

Table 5.1: Maximum, median, mean and minimum time per buﬀer for each exper-

iment

Experiment Maximum Median Mean Minimum

Trace, no delay
Trace, 100 µs delay
Synthetic Read/Write
instructions, no delay
Synthetic Read/Write
instructions, 100 µs delay
Synthetic Ping instructions,
no delay
Synthetic Ping instructions,
100 µs delay

15.0 ms
13.1 ms
17.0 ms

4.0 ms
4.0 ms
4.0 ms

6.7 ms
4.3 ms
8.6 ms

3.8 ms
3.7 ms
3.7 ms

16.1 ms

4.0 ms

4.5 ms

3.7 ms

59.1 ms

4.0 ms

22.6 ms

3.7 ms

64.0 ms

4.0 ms

8.9 ms

3.7 ms

Table 5.2: Maximum, median, mean and minimum time between buﬀers for each

experiment

54

5.2 Results

Experiment Eﬀective data rate Processing data rate

Trace, no delay
Trace, 100 µs delay
Synthetic Read/Write
instructions, no delay
Synthetic Read/Write
instructions, 100 µs delay
Synthetic Ping instructions,
no delay
Synthetic Ping instructions,
100 µs delay

1 600 717 bit/s
313 481 bit/s
1 600 717 bit/s

3 788 589 bit/s
4 306 544 bit/s
2 916 174 bit/s

314 027 bit/s

2 999 109 bit/s

534 118 bit/s

644 432 bit/s

314 027 bit/s

565 894 bit/s

Table 5.3: The eﬀective and processing data rates for each experiment. The ef-
fective data rate is the number of bits that were received divided by
the duration of the experiment (60 s). The processing data rate is the
rate at which the actual packet processing task could in theory process
packets. It is calculated by dividing the number of bits that were re-
ceived by the time spent processing them (the sum of all time per buﬀer
measurements).

55

6 Discussion

This chapter discusses the results gathered from the experiments that were pre-
sented and evaluated in chapter 5.

All of the experiments except for 5.2.5 and 5.2.6 showed a maximum time between
buﬀers of below or slightly above 16 ms. This means that in practice, the imple-
mentation is performant enough to not lose any data, especially considering that
a bus load of 100 % is not possible in reality.
It is clear that there is a constant overhead of about 4 ms in the time between
buﬀers. This overhead can be seen as the median time between buﬀers in all
experiments. This overhead is not small; compared to the approximate maximum
of 16 ms, it is 25 % of the entire time spent.
From both experiments that used synthetic Ping instructions as data it is apparent
that Ping instructions are the absolute worst case when it comes to processing time.
This is not surprising considering that Ping instructions may require allocating a
new ControlTable object (see subsection 4.2.6). However, these allocations are only
necessary when the model number changes constantly as was the case in these two
experiments. This is simply not a realistic scenario; in practice, Ping instructions
are incredibly rare, usually only sent when the master connects to the bus for the
ﬁrst time.
The number of Ping instructions in the other experiments was already higher than
to be expected because the data they used contained at least one Ping instruc-
tion and response for every device. This means that Ping instructions were sent
every time the data was repeated. This unusually high frequency did not impact
performance in any meaningful way, however. All four experiments processed the
incoming data in time.
Generally, the amount of load on the bus was noticeable when interacting with
the UI. It manifested as periodic increases in latency and low framerate. These
became especially severe when the load was too high to be processed in time.
This is a direct consequence of how the UI and the data processing task are conﬁg-
ured. Since the UI task is only assigned a ﬁxed amount of time after all incoming
data in one half of the buﬀer has been processed, higher processing times decrease
the overall amount of time spent updating the UI (see subsection 4.2.4 for details).
While this only seriously aﬀected the UI once incoming data was already getting
lost, the user experience was still not acceptable. There is certainly room for
improvement, either by optimizing the ﬁrmware, redesigning the way the priorities

57

6 Discussion

of the two tasks are handled or by switching to hardware with greater processing
power.

58

7 Conclusion and Future Work

This chapter gives a conclusion on the work done as well as the results presented
in section 7.1. Section 7.2 discusses possible future work.

7.1 Conclusion

In this thesis ﬁrmware for the STM32F7508-DK board has been developed that
allows monitoring and debugging the status of devices connected to a ROBOTIS
Dynamixel Protocol 2.0 based bus. The targeted Wolfgang robot platform uses
RS-485 but any bus compatible with a UART interface can be used. Like with
RS-485, a transceiver or converter has to be used to interface the bus with the
board itself. It is also possible to directly connect a bus using TTL logic levels
(3.3–5 V). This is eﬀectively what was done during testing and evaluation.
The STM32F7508-DK board is well suited for the development of graphical appli-
cations. Because the touchscreen display is already part of the board, no further
assembly was required. The speed of the STM32F750N8H6 microcontroller is suf-
ﬁcient but any less powerful hardware would most likely have caused serious issues.
A signiﬁcant amount of processing power is needed just to render and update the
UI.
The UI has been designed to clearly highlight any disconnected devices. Consistent
color coding (red for disconnected, green for connected) is used across all views.
The diﬀerent views allow users to select varying levels of detail. While the UI
performs well enough to be usable, there is noticeable lag, especially under high
load.
The ﬁrmware is performant enough to handle the data rate of 2 MBd used with
the Wolfgang robot platform. Future improvements would allow for even higher
data rates or multiple bus connections (see section 7.2).
The source code of the ﬁrmware makes it easy to add support for new device mod-
els or update the deﬁnition of already supported ones by constraining necessary
changes to one well-deﬁned interface. The code must be recompiled and ﬂashed
to the board to deploy changes.
Most of the ﬁrmware code is either platform-independent or uses the emWin li-
brary. Porting the ﬁrmware to diﬀerent (Arm Cortex-M based) hardware should
be possible with reasonable eﬀort: both bootloader and hardware initialization, as
well as the emWin and FreeRTOS conﬁguration, would have to modiﬁed.

59

7 Conclusion and Future Work

7.2 Future Work

There are various ways in which the current implementation can be improved:

• Currently, the device details view shows all ﬁelds in the device’s control table.
Only a small number of values for these ﬁelds are ever observed. There is no
way to diﬀerentiate a default value from a value that was actually observed.
Default values could be highlighted in a diﬀerent color or left out altogether.

• It should be possible to accept data from more than one RS-485 bus at the
same time without diﬃculties. Further investigation would be required on
how to physically connect additional buses. The increased data rate most
likely also requires performance improvements.

• Performance may be improved by increasing the size of the receive buﬀers.
This may also allow improving UI performance by increasing the yield time
of the data processing task.

• Performance may be improved by further optimizing the code and data struc-

tures used. This is unlikely to result in large improvements, however.

• Performance could also be improved by using more powerful hardware.

• Some display ﬂickering may be removed by enabling and using V-Sync with

the LCD controller.

• UI performance may be improved by using the dedicated 2D hardware ac-
celerator included in the STM32F750N8H6 microcontroller [STM18c]. This
is unlikely to have a noticeable eﬀect, as the UI task appears to spend most
of the time updating the state of the widgets.

• UI performance may be improved signiﬁcantly by using a dual-core CPU. A
dedicated CPU core could be used for rendering the UI, which would also
decrease latency and simplify the code since the data processing task would
not have to yield to allow for UI updates.

60

Bibliography

[bit19]

[cat]

[Coo]

Robots of the Hamburg Bit-Bots.
https://submission.robocuphumanoid.org/uploads/Hamburg_
Bit_Bots-specs-5de3cecc85cbe.pdf, 2019. Accessed: 2020-03-02.

Why do we need yet another C++ test framework?
https://github.com/catchorg/Catch2/blob/
87950d9cfa87eb41ff60b7e5f7e11ad21749a2a1/docs/why-
catch.md. Accessed: 2020-03-11.

Greg Cook. Catalogue of parametrised CRC algorithms with 16 bits.
http://reveng.sourceforge.net/crc-catalogue/16.htm.
Accessed: 2020-03-04.

[FAD+19] R´emi Fabre, Boris Albar, Cl´ement Dussieux, Ludwig Joﬀroy, Zhe Li,

Cl´ement Pinet, Jennifer Simeon, and S´ebastien Loty. CATIE
Robotics @Home 2019 Team Description Paper. Technical report,
Centre Aquitain des Technologies de l’Information et Electroniques,
1 Avenue du Dr Albert Schweitzer, 33400 Talence, France, 2019.

[frea]

[freb]

[frec]

[fred]

[free]

Memory Management. https://www.freertos.org/a00111.html.
Accessed: 2020-03-11.

RTOS Fundamentals.
https://www.freertos.org/implementation/a00002.html.
Accessed: 2020-03-06.

Running the RTOS on a ARM Cortex-M Core.
https://www.freertos.org/RTOS-Cortex-M3-M4.html. Accessed:
2020-03-11.

The FreeRTOSTM Kernel. https://www.freertos.org/RTOS.html.
Accessed: 2020-03-11.

xsemaphorecreatemutex.
https://www.freertos.org/CreateMutex.html. Accessed:
2020-03-11.

61

Bibliography

[Fre16]

Free Software Foundation. LD(1) Linux User’s Manual, October
2016. Part of binutils-arm-none-eabi 2.27.

[Fut]

[iro]

[Max14]

Future Technology Devices International. Future Technology Devices
International Ltd. FT232R USB UART IC Datasheet. Version 2.15.

irobot: Saug-, Wisch- und M¨ahroboter. https://www.irobot.de/.
Accessed: 2020-03-17.

Maxim Integrated.
MAX481/MAX483/MAX485/MAX487–MAX491/MAX1487
Low-Power, Slew-Rate-Limited RS-485/RS-422 Transceivers,
September 2014. Revision 10.

[MMW+19] Raphael Memmesheimer, Ivanna Mykhalchyshyna, Niklas Yann
Wettengel, Tobias Evers, Lukas Buchhold, Patrik Schmidt, Niko
Schmidt, Ida Germann, Mark Mints, Greta Rettler, Christian
Korbach, Robin Bartsch, Isabelle Kuhlmann, Thomas Weiland, and
Dietrich Paulus. RoboCup 2019 - homer@UniKoblenz (Germany).
Technical report, University of Koblenz-Landau, Universit¨atsstr. 1,
56070 Koblenz, Germany, 2019.

[new]

[PG18]

The Red Hat newlib C Library.
https://sourceware.org/newlib/libc.html. Accessed:
2020-03-11.

A. K. Pandey and R. Gelin. A Mass-Produced Sociable Humanoid
Robot: Pepper: The First Machine of Its Kind. IEEE Robotics
Automation Magazine, 25(3):40–48, 2018.

[PMM+19] Bruno F. V. Perez, Douglas R. Meneghetti, Enrico Matiuci,
Leonardo C. Neves, Fagner Pimentel, Gabriel S. Melo, Jo˜ao
Victor M. Santos, Lucas I. Gazignato, Marina Y. Gonbata,
Mateus G. Carvalho, Matheus V. Domingos, Rodrigo C. Techi,
Thiago S. B. Meyer, William Y. Yaguiu, Flavio Tonidandel,
Reinaldo Bianchi, and Plinio T. Aquino Junior. RoboFEI@Home
Team Description Paper for RoboCup@Home 2019. Technical
report, FEI University Center, Sao Paulo, Brazil, 2019.

A Brief History of RoboCup.
https://www.robocup.org/a_brief_history_of_robocup.
Accessed: 2020-03-24.

[roba]

62

Bibliography

[robb]

[robc]

[robd]

[ROBe]

Objective. https://www.robocup.org/objective. Accessed:
2020-03-24.

Qualiﬁed teams for RoboCup 2019.
https://humanoid.robocup.org/hl-2019/teams/. Accessed:
2020-03-17.

RoboCupSoccer. https://www.robocup.org/domains/1. Accessed:
2020-03-24.

ROBOTIS. Protocol 2.0.
http://emanual.robotis.com/docs/en/dxl/protocol2/.
Accessed: 2020-03-01.

[RWT+19] Prof. Dr. Matthias R¨atsch, Thomas Weber, Sergey Triputen, Marvin
Ott, Peter Stengl, Pengfei Huyan, Bo Zhang, He Lin, Steﬀen Eißler,
Michael Litz, Moritz M¨ahr, Lennart Kraft, Le Ping Peng, P¨aivi
K¨arn¨a, Patrik Huber, and Michael Danner. RT Lions Team
Description Paper. Technical report, Reutlingen University,
Alteburgstraße 150, 72762 Reutlingen, Germany, 2019.

[SEG17]

SEGGER Microcontroller GmbH & Co. KG. emWin - Graphic
Library with Graphical User Interface - User & Reference Guide,
November 2017. UM03001 Revision 1, part of STM32CubeF7 1.15.0.

[STM17]

STMicroelectronics. UM1905 User Manual - Description of
STM32F7 HAL and Low-layer drivers, February 2017. Revision 3.

[STM18a]

STMicroelectronics. DS12535 datasheet - STM32F750x8, June 2018.
Revision 1.

[STM18b]

STMicroelectronics. Release Notes for STemWin Library, March
2018. Part of STM32CubeF7 1.15.0.

[STM18c]

STMicroelectronics. RM0385 Reference manual - STM32F75xxx and
STM32F74xxx advanced Arm R(cid:13)-based 32-bit MCUs, June 2018.
Revision 8.

[STM18d]

STMicroelectronics. UM2470 User manual - Discovery kit for
STM32F7 Series with STM32F750N8 MCU, October 2018. Revision
1.

[STM19a]

STMicroelectronics. UM1734 User manual - STM32CubeTM USB
device library, February 2019. Revision 4.

63

Bibliography

[STM19b]

STMicroelectronics. UM1891 User manual - Getting started with
STM32CubeF7 MCU Package for STM32F7 Series, January 2019.
Revision 9.

[SZC02]

Manny Soltero, Jing Zhang, and Chris Cockril. RS-422 and RS-485
Standards Overview and System Conﬁgurations. Technical report,
Texas Instruments, June 2002. Revised May 2010.

[TB14]

Andrew S. Tanenbaum and Herbert Bos. Modern Operating
Systems, pages 37–38. Pearson, fourth edition, 2014.

[usb00]

Universal Serial Bus Speciﬁcation Revision 2.0, April 2000.

[YTO+19] Takashi Yamamoto, Yutaro Takagi, Akiyoshi Ochiai, Kunihiro

Iwamoto, Yuta Itozawa, Yoshiaki Asahara, Yasukata Yokochi, and
Koichi Ikeda. Human Support Robot as Research Platform of
Domestic Mobile Manipulator. Technical report, Toyota Frontier
Research Center and Toyota Research Institute, 2019.

64

Eidesstattliche Erkl¨arung

Hiermit versichere ich an Eides statt, dass ich die vorliegende Arbeit im Bach-
elorstudiengang Informatik selbstst¨andig verfasst und keine anderen als die
angegebenen Hilfsmittel – insbesondere keine im Quellenverzeichnis nicht be-
nannten Internet-Quellen – benutzt habe. Alle Stellen, die w¨ortlich oder sin-
ngem¨aß aus Ver¨oﬀentlichungen entnommen wurden, sind als solche kenntlich
gemacht. Ich versichere weiterhin, dass ich die Arbeit vorher nicht in einem an-
deren Pr¨ufungsverfahren eingereicht habe und die eingereichte schriftliche Fassung
der auf dem elektronischen Speichermedium entspricht.

Hamburg, den 29.04.2020

Robin Mirow

Ver¨oﬀentlichung

Ich stimme der Einstellung der Arbeit in die Bibliothek des Fachbereichs Infor-
matik zu.

Hamburg, den 29.04.2020

Robin Mirow


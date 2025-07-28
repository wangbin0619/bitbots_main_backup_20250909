#!/usr/bin/env python3
"""
Analysis of vcstool usage in the Bit-Bots project
"""

import yaml
import os

def analyze_workspace_repos():
    """Analyze the workspace.repos file to understand vcstool usage"""
    
    print("=== VCSTOOL (VCS Tool) Analysis for Bit-Bots Project ===\n")
    
    # Read the workspace.repos file
    workspace_file = "D:/20-robot/01-bitbots/workspace.repos"
    
    if not os.path.exists(workspace_file):
        print("ERROR: workspace.repos file not found!")
        return
        
    with open(workspace_file, 'r') as f:
        workspace_data = yaml.safe_load(f)
    
    repositories = workspace_data.get('repositories', {})
    
    print(f"SUMMARY:")
    print(f"   - Total external repositories managed: {len(repositories)}")
    print(f"   - All repositories use Git as VCS type")
    print(f"   - Repositories are organized in lib/ and specific paths\n")
    
    print("WHAT VCSTOOL DOES:")
    print("   - Multi-repository management tool for ROS/robotics projects")
    print("   - Manages collections of Git repositories as a single workspace")
    print("   - Handles dependencies across multiple repositories\n")
    
    print("REPOSITORY CATEGORIES:")
    
    lib_repos = []
    other_repos = []
    
    for repo_path, repo_info in repositories.items():
        if repo_path.startswith('lib/'):
            lib_repos.append((repo_path, repo_info))
        else:
            other_repos.append((repo_path, repo_info))
    
    print(f"\n   LIB/ DEPENDENCIES ({len(lib_repos)} repositories):")
    for path, info in lib_repos:
        repo_name = path.split('/')[-1]
        print(f"      - {repo_name:<25} | {info['url'].split('/')[-1].replace('.git', '')}")
    
    print(f"\n   OTHER COMPONENTS ({len(other_repos)} repositories):")
    for path, info in other_repos:
        print(f"      - {path:<45} | {info['url'].split('/')[-1].replace('.git', '')}")
    
    print("\n MAKEFILE COMMANDS USING VCSTOOL:")
    makefile_commands = [
        ("make pull-repos", "vcs pull . --nested", "Pull updates from all repositories"),
        ("make setup-libs", "vcs import . < workspace.repos", "Clone all repositories defined in workspace.repos"),
        ("make status", "vcs status . --nested", "Show git status of all repositories"),
    ]
    
    for make_cmd, vcs_cmd, description in makefile_commands:
        print(f"   - {make_cmd:<20} → {vcs_cmd:<30} | {description}")
    
    print("\n WARNING - WITHOUT VCSTOOL:")
    print("   - Cannot automatically manage 22+ external dependencies")
    print("   - Manual git operations required for each repository")
    print("   - Risk of version mismatches between repositories")
    print("   - Build system may fail due to missing dependencies")
    
    print("\n SOLUTION:")
    print("   - Install: pip install vcstool")
    print("   - Verify: vcs --version")
    print("   - Then run: make pull-all or make setup-libs")

if __name__ == "__main__":
    analyze_workspace_repos()
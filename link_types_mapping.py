#!/usr/bin/env python3
"""
Test script to create comprehensive link type mappings based on common Jira configurations.
"""

import json

# Common Jira link types based on standard installations and plugins
STANDARD_LINK_TYPES = [
    {
        "name": "Blocks",
        "inward": "is blocked by",
        "outward": "blocks"
    },
    {
        "name": "Cloners", 
        "inward": "is cloned by",
        "outward": "clones"
    },
    {
        "name": "Duplicate",
        "inward": "is duplicated by", 
        "outward": "duplicates"
    },
    {
        "name": "Relates",
        "inward": "relates to",
        "outward": "relates to"
    },
    {
        "name": "Causes",
        "inward": "is caused by",
        "outward": "causes"
    },
    {
        "name": "Gantt Dependency",
        "inward": "has to be finished together with",
        "outward": "has to be finished together with"
    },
    {
        "name": "Gantt Start to Finish",
        "inward": "has to be done after",
        "outward": "has to be done before"
    },
    {
        "name": "Gantt Start to Start", 
        "inward": "has to be started together with",
        "outward": "has to be started together with"
    },
    {
        "name": "Gantt Finish to Finish",
        "inward": "earliest end is start of",
        "outward": "start is earliest end of"
    },
    {
        "name": "Gantt Finish to Start",
        "inward": "has to be started",
        "outward": "has to be finished before start of"
    },
    {
        "name": "Hierarchy",
        "inward": "is child of",
        "outward": "is parent of"
    },
    {
        "name": "Idea",
        "inward": "added to idea",
        "outward": "is idea for"
    },
    {
        "name": "Merge",
        "inward": "merged into",
        "outward": "merged from"
    },
    {
        "name": "Implements",
        "inward": "is implemented by",
        "outward": "implements"
    },
    {
        "name": "Risk Mitigation",
        "inward": "is mitigated by",
        "outward": "mitigates risk"
    },
    {
        "name": "Split",
        "inward": "split from",
        "outward": "split to"
    }
]

def create_mapping():
    """Create mapping from UI descriptions to link type parameters."""
    
    ui_descriptions = [
        "is blocked by", "blocks", "is cloned by", "clones", 
        "is duplicated by", "duplicates", "has to be finished together with",
        "has to be done after", "has to be done before", 
        "earliest end is start of", "start is earliest end of",
        "has to be started", "is child of", "is parent of",
        "added to idea", "is idea for", "merged into", "merged from",
        "is implemented by", "implements", "is caused by", "causes",
        "relates to", "is mitigated by", "mitigates risk",
        "split from", "split to"
    ]
    
    print("=== JIRA LINK TYPES MAPPING ===\n")
    print("Based on standard Jira installations and common plugins:\n")
    
    mapping = {}
    
    for desc in ui_descriptions:
        found = False
        for link_type in STANDARD_LINK_TYPES:
            if desc.lower() == link_type["inward"].lower() or desc.lower() == link_type["outward"].lower():
                parameter = link_type["name"]
                mapping[desc] = parameter
                print(f"'{desc}' → Parameter: '{parameter}'")
                found = True
                break
        
        if not found:
            # Try partial matches for complex descriptions
            for link_type in STANDARD_LINK_TYPES:
                if any(word in link_type["inward"].lower() for word in desc.lower().split()) or \
                   any(word in link_type["outward"].lower() for word in desc.lower().split()):
                    parameter = link_type["name"]
                    mapping[desc] = parameter
                    print(f"'{desc}' → Parameter: '{parameter}' (partial match)")
                    found = True
                    break
            
            if not found:
                mapping[desc] = "NOT_FOUND"
                print(f"'{desc}' → NOT FOUND - may be custom or plugin-specific")
    
    print(f"\n=== SUMMARY ===")
    print(f"Total UI descriptions: {len(ui_descriptions)}")
    print(f"Mapped: {len([v for v in mapping.values() if v != 'NOT_FOUND'])}")
    print(f"Not found: {len([v for v in mapping.values() if v == 'NOT_FOUND'])}")
    
    print(f"\n=== USAGE EXAMPLES ===")
    print("For jira_create_issue_link tool:")
    for desc, param in list(mapping.items())[:3]:
        if param != "NOT_FOUND":
            print(f"""
{{
  "link_type": "{param}",
  "inward_issue_key": "PROJ-123", 
  "outward_issue_key": "PROJ-456"
}}""")
    
    return mapping

if __name__ == "__main__":
    create_mapping()
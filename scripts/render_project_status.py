#!/usr/bin/env python3
"""Render state projections; --check fails on stale projections without writing."""
import argparse
from pathlib import Path
from project_state import ROOT,managed_views,replace_block

def render(root=ROOT,check=False):
    stale=[]
    for path,name,body in managed_views(root):
        old=(root/path).read_text();new=replace_block(old,name,body)
        if old!=new:
            stale.append(path)
            if not check:(root/path).write_text(new)
    return stale
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');p.add_argument('--root',type=Path,default=ROOT);a=p.parse_args()
    stale=render(a.root,a.check)
    print(('Stale views: ' if a.check else 'Rendered views: ')+', '.join(stale) if stale else 'Current-state views are synchronized.')
    raise SystemExit(1 if a.check and stale else 0)

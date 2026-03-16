#!/usr/bin/env python3
"""Minesweeper game."""
import random,argparse
class Minesweeper:
    def __init__(s,w=10,h=10,mines=10):
        s.w=w;s.h=h;s.board=[[0]*w for _ in range(h)];s.revealed=[[False]*w for _ in range(h)];s.flagged=[[False]*w for _ in range(h)]
        positions=random.sample([(r,c) for r in range(h) for c in range(w)],mines)
        for r,c in positions: s.board[r][c]=-1
        for r in range(h):
            for c in range(w):
                if s.board[r][c]!=-1:
                    s.board[r][c]=sum(1 for dr in(-1,0,1) for dc in(-1,0,1) if 0<=r+dr<h and 0<=c+dc<w and s.board[r+dr][c+dc]==-1)
    def reveal(s,r,c):
        if s.revealed[r][c] or s.flagged[r][c]: return
        s.revealed[r][c]=True
        if s.board[r][c]==-1: return False
        if s.board[r][c]==0:
            for dr in(-1,0,1):
                for dc in(-1,0,1):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<s.h and 0<=nc<s.w: s.reveal(nr,nc)
        return True
    def display(s):
        print("  "+"".join(f"{c:2d}" for c in range(s.w)))
        for r in range(s.h):
            row=f"{r:2d}"
            for c in range(s.w):
                if s.flagged[r][c]: row+=" F"
                elif not s.revealed[r][c]: row+=" ."
                elif s.board[r][c]==-1: row+=" *"
                elif s.board[r][c]==0: row+="  "
                else: row+=f" {s.board[r][c]}"
            print(row)
    def won(s): return all(s.revealed[r][c] or s.board[r][c]==-1 for r in range(s.h) for c in range(s.w))
def main():
    p=argparse.ArgumentParser();p.add_argument("-w",type=int,default=10);p.add_argument("--height",type=int,default=10);p.add_argument("-m","--mines",type=int,default=10)
    a=p.parse_args();g=Minesweeper(a.w,a.height,a.mines)
    while True:
        g.display()
        try: cmd=input("r/f row col: ").split()
        except EOFError: break
        if len(cmd)<3: continue
        action,r,c=cmd[0],int(cmd[1]),int(cmd[2])
        if action=="f": g.flagged[r][c]=not g.flagged[r][c]
        elif action=="r":
            if not g.reveal(r,c): g.display();print("BOOM! Game over.");break
        if g.won(): g.display();print("You win!");break
if __name__=="__main__": main()

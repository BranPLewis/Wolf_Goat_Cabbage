import argparse
from wgc import bfs, ids, init_state

def main():
    parser = argparse.ArgumentParser(description="Wolf, Goat, and Cabbage Problem Solver")
    parser.add_argument('--algo', choices=['bfs', 'ids'], default='bfs', help='Search method to use (default: bfs)')
    parser.add_argument('--domain', choices=['wgc'], default='wgc', help='Problem domain (default: wgc)')
    args = parser.parse_args()
    
    if args.domain == 'wgc':
        print("Domain: Wolf, Goat, and Cabbage Problem")
        pos = ["start bank", "target bank"]
        if args.algo == 'bfs':
            path, queue_size, t_nodes, e_nodes = bfs(init_state)
        else:
            path = ids(init_state)
        if path:
            if args.algo == 'bfs':
                print('algorithm: BFS')
                print(f"Max queue size: {queue_size}")
                print(f"Total nodes generated: {t_nodes}")
                print(f"Total expanded nodes: {e_nodes}\n")
                print(f"(Farmer, Wolf, Goat, Cabbage)\n")
                print(f"if 0's change to 1's or 1's to 0's, they have been moved across the river\n")
                print(f"0 = start bank, 1 = target bank\n")
            else:
                print('algorithm: IDS')
            for i, state in enumerate(path):
                farmer, wolf, goat, cabbage = state
                print(f'Step {i}:\n ({farmer},{wolf},{goat},{cabbage})\n Farmer: {pos[farmer]}\n Wolf: {pos[wolf]}\n Goat: {pos[goat]}\n Cabbage: {pos[cabbage]}\n---------------------\n')
        else:
            print("No path found")

if __name__ == "__main__":
    main()
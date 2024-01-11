import argparse
from bmrt_context import batch_bmrt_context

def main():
    parser = argparse.ArgumentParser(description='Your program description')
    parser.add_argument('--context_root', help='Specify the context root')
    parser.add_argument('--bmodel_root', help='Specify the bmodel root')
    args = parser.parse_args()

    if not (args.context_root is None) ^ (args.bmodel_root is None):
        parser.error('Please provide either --context_root or --bmodel_root, but not both.')

    if args.context_root:
        batch_bmrt_context(args.context_root)

if __name__ == '__main__':
    main()

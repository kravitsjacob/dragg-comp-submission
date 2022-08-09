import asyncio 
import sys
from dragg_comp.rl_aggregator import RLAggregator
import argparse

REDIS_URL = "redis://redis"

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", help="Start date", default=None)
    parser.add_argument("-e", "--end", help="End date", default=None)
    parser.add_argument("-r", "--redis", help="Redis host URL", default=REDIS_URL)

    args = parser.parse_args()

    # if len(sys.argv)>1:
    a = RLAggregator(args.start, args.end, args.redis)
    # else:
    #     a = RLAggregator()
    asyncio.run(a.open_server())
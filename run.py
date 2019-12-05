from src.speedtestShipper import speedtestShipper
from argparse import ArgumentParser
from sys import argv

def main():

    print("""\
 _____                     _ _            _     _____ _     _                        
/  ___|                   | | |          | |   /  ___| |   (_)                       
\ `--. _ __   ___  ___  __| | |_ ___  ___| |_  \ `--.| |__  _ _ __  _ __   ___ _ __  
 `--. \ '_ \ / _ \/ _ \/ _` | __/ _ \/ __| __|  `--. \ '_ \| | '_ \| '_ \ / _ \ '__| 
/\__/ / |_) |  __/  __/ (_| | ||  __/\__ \ |_  /\__/ / | | | | |_) | |_) |  __/ |    
\____/| .__/ \___|\___|\__,_|\__\___||___/\__| \____/|_| |_|_| .__/| .__/ \___|_|    
      | |                                                    | |   | |               
      |_|                                                    |_|   |_|                  
      """)
    parser = ArgumentParser(description='Run SpeedtestCLI and push data to AWS ES', usage='python ' + argv[0] + ' --verbose=yes --add_cron_job=yes')
    parser.add_argument('--add_cron_job', default='no', help='Use cronjob for streaming data, use \'yes\' or \'no\' (default: no)')
    parser.add_argument('--verbose', default='no', help='View the script opening chrome, use \'yes\' or \'no\' (default: no)')

    if len(argv) < 2:
        print(parser.print_help())
    else :
        args = parser.parse_args()
        while True:
            speedtestShipper(args.verbose)
        #if args.add_cron_job == 'yes':
            #Crontab()

if __name__ == "__main__":
    main()
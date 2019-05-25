import sys, os
from dotenv import load_dotenv
load_dotenv()
OUTPUTDIR = os.path.join(sys.path[0], 'output')
S3_BUCKET = os.getenv('S3_BUCKET')
os.system('aws s3 sync %s s3://%s --acl public-read --delete' % (OUTPUTDIR, S3_BUCKET))

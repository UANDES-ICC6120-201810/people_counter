AWS_REGION = 'nyc3'
AWS_ACCESS_KEY_ID = 'OETLUPZHGGEULW6H5ASU'
AWS_SECRET_ACCESS_KEY = '0yVwkRTRWm5d/+JGQCAirmZFXRUQwZBElfZ8EJkNVSs'
AWS_STORAGE_BUCKET_NAME = 'zapo-storage'
AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'
AWS_LOCATION = 'occupation_images'


STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
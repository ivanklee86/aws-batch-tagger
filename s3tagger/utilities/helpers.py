import datetime
import urllib

def key_to_data(bucket: str, key: str, date: datetime.datetime) -> dict:
    (_, build, _) = key.split("/")
    (version, build_number) = build.split("_")

    return {
        'text': f'{version} ({build_number}) - Built on {date.strftime("%m/%d/%Y %H:%M:%S %Z")}',
        'url': f'https://{bucket}.s3.amazonaws.com/{key}',
        'encoded_url': urllib.parse.quote_plus(f'https://{bucket}.s3.amazonaws.com/{key}'),  # type: ignore
        'created_on': date
    }

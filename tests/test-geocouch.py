import sys
import json
import requests

_db="test"
_host="127.0.0.1"
_port=5984

try:
    # create db
    r = requests.put("http://{h}:{p}/{db}".format(h=_host, p=_port, db=_db))
    r.raise_for_status()

    _spatial_fn = """\
    {
        "spatial": {
            "points": "function(doc) {if (doc.loc) {emit({type: 'Point',coordinates: [doc.loc[0], doc.loc[1]]}, [doc._id, doc.loc]);}};"
        }
    }
    """

    # add spatial func
    r = requests.put("http://{h}:{p}/{db}/_design/main".format(h=_host, p=_port, db=_db), data=_spatial_fn)
    r.raise_for_status()

    _docs = {
        "oakland": '{"loc": [-122.270833, 37.804444]}',
        "augsburg": '{"loc": [10.898333, 48.371667]}',
    }

    for city, coordinates in _docs.items():
        r = requests.put("http://{h}:{p}/{db}/{doc}".format(h=_host, p=_port, db=_db, doc=city), data=coordinates)
        r.raise_for_status()

    r = requests.get("http://{h}:{p}/{db}/_design/main/_spatial/points?bbox=0,0,180,90".format(h=_host, p=_port, db=_db))
    r.raise_for_status()

    j = json.loads(r.content)

    assert j["rows"][0]["id"] == 'augsburg'
except Exception as e:
    print e
    print "Geocouch not working properly.\r\n";
    sys.exit(1)
else:
    print "It is working!\r\n";
    sys.exit(0)
finally:
    r = requests.delete("http://{h}:{p}/{db}".format(h=_host, p=_port, db=_db))

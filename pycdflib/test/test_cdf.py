import pytest
import shutil,os,tempfile
import requests
import datetime
from pycdflib.cdf import ReadOnlyCDF

def download_test_cdf_file(destfn):
    base_url = 'https://spdf.gsfc.nasa.gov/pub/data/omni/omni_cdaweb/hourly/' 
    url = base_url+'2015/omni2_h0_mrg1hr_20150101_v01.cdf'
    response = requests.get(url,allow_redirects=True)
    with open(destfn,'wb') as f:
        f.write(response.content)

@pytest.fixture(scope='module')
def nasa_omniweb_cdf_file(request):

    cdfdir = tempfile.mkdtemp()
    cdffn = os.path.join(cdfdir,'test.cdf')

    download_test_cdf_file(cdffn)
    
    def remove_temporary_dir():
        shutil.rmtree(cdfdir)

    request.addfinalizer(remove_temporary_dir)

    return cdffn

def test_epoch_load(nasa_omniweb_cdf_file):
    cdf = ReadOnlyCDF(nasa_omniweb_cdf_file)
    dts = cdf['Epoch']
    assert isinstance(dts[0],datetime.datetime)



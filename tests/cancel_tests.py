from data import Data
import pytest
import helper
from api.cancel import Cancel



class TestCancel:

    reasons = ['OK','CANCELED','CLIENT_REFUSED','CLIENT_NOSMS','CLIENT_NOEMAIL','CLIENT_PASSPORT','CLIENT_NO_INFO','CANCEL_BY_TIMER']
    source_value = ['CRM_VOLGA_V2', 'CRM_SOUTH_V2', 'CRM_URAL_V2', 'CRM_NORTH_WEST_V2', 'CRM_FAR_EAST_V2',
                    'CRM_SIBERIA_V2']
    type_task = ['CONTRACT', 'CONTRACT_ALADDIN', 'PAID_WORK_ACT', 'CONTRACT_MEGAFON']

    @pytest.mark.parametrize('source_value', source_value)
    @pytest.mark.parametrize('type_task', type_task)
    @pytest.mark.parametrize('reasons', reasons)
    def test_create_for_all_process(self, source_value, type_task, reasons):
        data = helper.ChangeTestDataHelper.modify_payload_body(Data.data_contract, source_value, type_task)
        response = Cancel.cancel(data, reasons)

        assert response.status_code == 200 and response.json() is not None


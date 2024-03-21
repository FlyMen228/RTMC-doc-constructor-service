function toggleFields() {

    var selectValue = document.getElementById('templateType').value;
    var withoutOrganization = document.getElementById('withoutOrganizationField');
    var withOrganization = document.getElementById('withOrganizationFields');

    withoutOrganization.style.display = 'none';
    withOrganization.style.display = 'none';

    if (selectValue === 'withoutOrg') {
        withoutOrganization.style.display = 'block';
    } else if (selectValue === 'withOrg') {
        withOrganization.style.display = 'block';
    }

}
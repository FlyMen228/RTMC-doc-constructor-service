document.addEventListener("DOMContentLoaded", function () {
    window.toggleFields = function toggleFields() {
        var select_value = document.getElementById('load_type').value;

        var one = document.getElementById('load_one');
        var many = document.getElementById('load_many');

        one.style.display = 'none';
        many.style.display = 'none';

        if (select_value === 's') {
            one.style.display = 'block';
        } else if (select_value === 'm') {
            many.style.display = 'block';
        }
    }
});
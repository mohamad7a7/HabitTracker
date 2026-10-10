
document.addEventListener('DOMContentLoaded', function () {
    const frequencyField = document.getElementById('id_frequency');

    const fieldNames = [
        'once_date',
        'start_date',
        'day_of_month',
        'time'
    ];

    function getFieldContainer(name) {
        const field = document.getElementById('id_' + name);

        if (!field) {
            return null;
        }

        return field.closest('p');
    }

    function updateFields() {
        const frequency = frequencyField.value;

        // ابتدا تمام فیلدهای وابسته را مخفی می‌کنیم
        fieldNames.forEach(function (name) {
            const container = getFieldContainer(name);

            if (container) {
                container.style.display = 'none';
            }
        });

        // مشخص می‌کنیم هر نوع Habit کدام فیلدها را لازم دارد
        let fieldsToShow = [];

        if (frequency === 'O') {
            fieldsToShow = ['once_date', 'time'];
        } else if (frequency === 'D') {
            fieldsToShow = ['start_date', 'time'];
        } else if (frequency === 'M') {
            fieldsToShow = ['day_of_month', 'time'];
        }

        // فقط فیلدهای موردنیاز را نمایش می‌دهیم
        fieldsToShow.forEach(function (name) {
            const container = getFieldContainer(name);

            if (container) {
                container.style.display = '';
            }
        });
    }

    frequencyField.addEventListener('change', updateFields);

    // هنگام باز شدن صفحه هم فیلدها را تنظیم می‌کنیم
    updateFields();
});
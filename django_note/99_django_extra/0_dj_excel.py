# pip install openpyxl
# view>>>>
""" 
from django.shortcuts import render
from .models import YourModel

def your_view(request):
    data = YourModel.objects.all()
    return render(request, 'your_template.html', {'data': data})
 """
# excel view>>>> #######################

""" 
from django.http import HttpResponse
from openpyxl import Workbook
def export_data(request):
    data = YourModel.objects.all()

    # Create an Excel workbook
    workbook = Workbook()
    sheet = workbook.active

# Write headers
    sheet['A1'] = 'Column 1'
    sheet['B1'] = 'Column 2'
    # Add more columns as needed

    # Write data
    for i, item in enumerate(data, start=2):
        sheet[f'A{i}'] = item.field1
        sheet[f'B{i}'] = item.field2
        # Add more columns as needed

    # Create response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=your_data.xlsx'
    workbook.save(response)
    return response
 """
# html>>>>
""" 
<table>
    <thead>
        <tr>
            <th>Column 1</th>
            <th>Column 2</th>
        </tr>
    </thead>
    <tbody>
        {% for item in data %}
            <tr>
                <td>{{ item.field1 }}</td>
                <td>{{ item.field2 }}</td>
            </tr>
        {% endfor %}
    </tbody>
</table>
 """
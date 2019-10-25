import yaml
from easysettings import YAMLSettings

# Bắt đầu từ đầu: tạo file
ys = YAMLSettings(filename='myfile.yaml')

# đặt giá trị biến cần lưu:
ys['bien1'] = 'gia tri 1'
ys['bien2'] = 2
ys['bien3'] = [1,2,3,4,5]

ys.save() # lưu file 

#------------------------------------------------------
!ls
# đọc thử nội dung xem file có gì?
!cat 'myfile.yaml'
#------------------------------------------------------

# Một chỗ nào đó, Load file mang các biến đã lưu ra dùng
from easysettings import YAMLSettings, load_yaml_settings

ys = load_yaml_settings('myfile.yaml', default={'option': 'mydefault'})
print('bien1=',ys['bien1'])
print('bien2=',ys['bien2'], type(ys['bien2']) )
print('bien3=',ys['bien3'])

# Thêm biến mới muốn lưu
ys['option2']= 'value2'
ys.save()

# cách khác để load file 
ys = YAMLSettings.from_file('myfile.yaml')
#------------------------------------------------------
# đọc lại nội dung file xem có cập nhật giá trị mới chưa?
!cat myfile.yaml

import input_data
import write_data
import output_data



def vybor(n):
    write_data.check_row1()
    if n == '1':
        return write_data.get_new_write(input_data.get_input_data())
    elif n == '2':
        return output_data.get_output_data()
    elif n == '3':
        return output_data.get_output_name()

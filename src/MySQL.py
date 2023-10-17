import csv
import datetime

import mysql.connector
from ConfigFile import *
from mysql.connector import errorcode

print("PP_database")


class MY_SQL:
    def __init__(self):
        self.cursor = 0
        self.cnx = 0
        self.CONNECT_DATABASE()

    def CONNECT_DATABASE(self):
        try:
            user = SettingRead('SETTING')['db user']
            password = SettingRead('SETTING')['db password']
            self.cnx = mysql.connector.connect(user=user, password=password, host='127.0.0.1', database='db_ate_pp')
            print("Database connected!")
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:

            self.cnx.rollback()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def SQL_SELECT_TOP_QUERY(self, selColName, tblName):

        pwd = 0
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character

        selectQry = "SELECT %s FROM %s ORDER BY %s DESC LIMIT 1  \
               " % (selColName, tblName, selColName)
        print
        selectQry
        self.cursor.execute(selectQry)

        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        for col in result:
            pwd = col[0]
            # Now print fetched result
            # print pwd
        self.cursor.close()
        return pwd

    def SQL_SELECT_LIST_2_QUERY(self, selColName, tblName, condition1, conditionValue1, condition2, conditionValue2):
        RESULT = []
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character
        selectQry = "SELECT %s FROM %s WHERE %s='%s' AND %s='%s' \
               " % (selColName, tblName, condition1, conditionValue1, condition2, conditionValue2)
        print
        selectQry
        self.cursor.execute(selectQry)
        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        # print result

        for col in result:
            temp = col[0]
            # print "temp: "+str(temp)
            RESULT.append(str(temp))
            # Now print fetched result
            # print RESULT
        self.cursor.close()
        return RESULT

    def SQL_SELECT_2_QUERY(self, selColName, tblName, condition1, conditionValue1, condition2, conditionValue2):
        pwd = 0
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character

        selectQry = "SELECT %s FROM %s WHERE %s='%s' AND %s='%s' \
               " % (selColName, tblName, condition1, conditionValue1, condition2, conditionValue2)
        print
        selectQry
        self.cursor.execute(selectQry)
        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        for col in result:
            pwd = col[0]
            # Now print fetched result
            # print pwd
        self.cursor.close()
        return pwd

    def SQL_SELECT_LIST_QUERY(self, selColName, tblName, condition1, conditionValue1):
        RESULT = []
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character
        selectQry = "SELECT %s FROM %s WHERE %s='%s' \
               " % (selColName, tblName, condition1, conditionValue1)
        print
        selectQry
        self.cursor.execute(selectQry)
        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        # print result
        for col in result:
            temp = col[0]
            # print "temp: "+str(temp)
            RESULT.append(str(temp))
            # Now print fetched result
            # print RESULT
        self.cursor.close()
        return RESULT

    def SQL_SELECT_QUERY(self, selColName, tblName, condition, conditionValue):

        pwd = 0
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character

        selectQry = "SELECT %s FROM %s WHERE %s='%s' \
               " % (selColName, tblName, condition, conditionValue)
        print
        selectQry
        self.cursor.execute(selectQry)

        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        for col in result:
            pwd = col[0]
            # Now print fetched result
            # print pwd
        self.cursor.close()

        return pwd

    def SQL_SELECT_LIST_2_QUERY(self, selColName, tblName, condition1, conditionValue1, condition2, conditionValue2):

        RESULT = []
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character

        selectQry = "SELECT %s FROM %s WHERE %s='%s' AND %s='%s' \
               " % (selColName, tblName, condition1, conditionValue1, condition2, conditionValue2)
        print
        selectQry
        self.cursor.execute(selectQry)
        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        # print result

        for col in result:
            temp = col[0]
            # print "temp: "+str(temp)
            RESULT.append(str(temp))
            # Now print fetched result
            # print RESULT
        self.cursor.close()
        return RESULT

    def SQL_SELECT_2_QUERY(self, selColName, tblName, condition1, conditionValue1, condition2, conditionValue2):

        pwd = 0
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character

        selectQry = "SELECT %s FROM %s WHERE %s='%s' AND %s='%s' \
               " % (selColName, tblName, condition1, conditionValue1, condition2, conditionValue2)
        print
        selectQry
        self.cursor.execute(selectQry)

        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        for col in result:
            pwd = col[0]
            # Now print fetched result
            # print pwd
        self.cursor.close()

        return pwd

    def SQL_SELECT_3_QUERY(self, selColName, tblName, condition1, conditionValue1, condition2, conditionValue2,
                           condition3, conditionValue3):

        pwd = 0
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character

        selectQry = "SELECT %s FROM %s WHERE %s='%s' AND %s='%s' AND %s='%s' \
               " % (
        selColName, tblName, condition1, conditionValue1, condition2, conditionValue2, condition3, conditionValue3)
        print
        selectQry
        self.cursor.execute(selectQry)

        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        for col in result:
            pwd = col[0]
            # Now print fetched result
            # print pwd
        self.cursor.close()

        return pwd

    def SQL_SELECT_4_QUERY(self, selColName, tblName, condition1, conditionValue1, condition2, conditionValue2,
                           condition3, conditionValue3, condition4, conditionValue4):

        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character

        selectQry = "SELECT %s FROM %s WHERE %s='%s' AND %s='%s' AND %s='%s' AND %s='%s' \
               " % (
        selColName, tblName, condition1, conditionValue1, condition2, conditionValue2, condition3, conditionValue3,
        condition4, conditionValue4)
        print
        selectQry
        self.cursor.execute(selectQry)

    def SQL_SELECT_5_QUERY(self, selColName, tblName, condition1, conditionValue1, condition2, conditionValue2,
                           condition3, conditionValue3, condition4, conditionValue4, condition5, conditionValue5):

        pwd = 0
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character

        selectQry = "SELECT %s FROM %s WHERE %s='%s' AND %s='%s' AND %s='%s' AND %s='%s' AND %s='%s' \
               " % (
        selColName, tblName, condition1, conditionValue1, condition2, conditionValue2, condition3, conditionValue3,
        condition4, conditionValue4, condition5, conditionValue5)
        print
        selectQry
        self.cursor.execute(selectQry)

        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        for col in result:
            pwd = col[0]
            # Now print fetched result
            # print pwd
        self.cursor.close()

        return pwd

    def SQL_REPORT_QUERY(self, pass_checked, fail_checked, part_number_checked, serial_number_checked, start_date,
                         end_date, mt_dut_partnumber, mt_dut_srno):
        global selectQry
        MT_ID = []
        self.cursor = self.cnx.cursor()
        # placeholders in a query: '%s' for string,'%d' for numbers,'%C' for character
        if pass_checked == 1 and fail_checked == 0 and part_number_checked == 1 and serial_number_checked == 0:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result= 'PASS' AND mt_dut_partnumber ='%s' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (mt_dut_partnumber, start_date, end_date)
        elif pass_checked == 1 and fail_checked == 0 and part_number_checked == 0 and serial_number_checked == 1:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result= 'PASS' AND mt_dut_srno ='%s' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (mt_dut_srno, start_date, end_date)
        elif pass_checked == 1 and fail_checked == 0 and part_number_checked == 1 and serial_number_checked == 1:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result= 'PASS' AND mt_dut_partnumber ='%s' AND mt_dut_srno='%s' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (mt_dut_partnumber, mt_dut_srno, start_date, end_date)
        elif pass_checked == 1 and fail_checked == 0 and part_number_checked == 0 and serial_number_checked == 0:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result= 'PASS' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (start_date, end_date)
        elif pass_checked == 0 and fail_checked == 1 and part_number_checked == 1 and serial_number_checked == 0:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result= 'FAIL' AND mt_dut_partnumber ='%s' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (mt_dut_partnumber, start_date, end_date)
        elif pass_checked == 0 and fail_checked == 1 and part_number_checked == 0 and serial_number_checked == 1:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result= 'FAIL' AND mt_dut_srno ='%s' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (mt_dut_srno, start_date, end_date)
        elif pass_checked == 0 and fail_checked == 1 and part_number_checked == 1 and serial_number_checked == 1:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result= 'FAIL' AND mt_dut_partnumber ='%s' AND mt_dut_srno='%s' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (mt_dut_partnumber, mt_dut_srno, start_date, end_date)
        elif pass_checked == 0 and fail_checked == 1 and part_number_checked == 0 and serial_number_checked == 0:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result= 'FAIL' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (start_date, end_date)
        elif part_number_checked == 1 and serial_number_checked == 0:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result is not null  and mt_result != 'HALTED' AND mt_dut_partnumber ='%s' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (mt_dut_partnumber, start_date, end_date)
        elif part_number_checked == 0 and serial_number_checked == 1:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result is not null  and mt_result != 'HALTED' AND mt_dut_srno ='%s' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (mt_dut_srno, start_date, end_date)
        elif part_number_checked == 1 and serial_number_checked == 1:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result is not null  and mt_result != 'HALTED' AND mt_dut_partnumber ='%s' AND mt_dut_srno='%s' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (mt_dut_partnumber, mt_dut_srno, start_date, end_date)
        elif part_number_checked == 0 and serial_number_checked == 0:
            selectQry = "SELECT mt_id FROM mst_test WHERE \
            mt_result is not null  and mt_result != 'HALTED' \
            AND mt_datetime IN(SELECT max(mt_datetime) FROM mst_test WHERE \
            mt_datetime BETWEEN '%s' AND '%s' GROUP BY mt_dut_srno, mt_dut_partnumber)\
            ORDER BY mt_id ASC" % (start_date, end_date)

        print(selectQry)
        self.cursor.execute(selectQry)
        # Fetch all the rows in a list of lists.
        result = self.cursor.fetchall()
        # print result

        for col in result:
            temp = col[0]
            # print "temp: "+str(temp)
            MT_ID.append(temp)
            # Now print fetched result
            # print MT_ID
        self.cursor.close()
        return MT_ID

    def SQL_MAIN_RUN_RECORD_INSERT_QUERY(self, mt_dut_partnumber, mt_dut_srno, mt_operator, mt_datetime, mt_testprogram,
                                         mt_customer, mt_config_ver):
        # insert Qry (for insert main test run records)
        self.cursor = self.cnx.cursor()
        dt = datetime.date.today()
        insertQry = "INSERT INTO mst_test(mt_dut_partnumber,mt_dut_srno,mt_operator,mt_datetime,mt_testprogram,mt_customer,mt_config_ver) \
        VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
        mt_dut_partnumber, mt_dut_srno, mt_operator, mt_datetime, mt_testprogram, mt_customer, mt_config_ver)

        print
        insertQry
        self.cursor.execute(insertQry)
        self.cnx.commit()
        self.cursor.close()

    def SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self, td_mt_id, td_test_item, td_readby, td_param_srno,
                                                      td_range_param, td_value_param, td_res_param):
        # insert Qry (for insert  test data records)
        self.cursor = self.cnx.cursor()
        dt = datetime.date.today()
        insertQry = "INSERT INTO test_detail_results(td_mt_id,td_test_item,td_readby,td_param_srno, \
        td_range_param,td_value_param,td_res_param) \
        VALUES (%d,%s,%s,%s,%s,%s,%s)" % (
        td_mt_id, td_test_item, td_readby, td_param_srno, td_range_param, td_value_param, td_res_param)

        print
        insertQry
        self.cursor.execute(insertQry)
        self.cnx.commit()
        self.cursor.close()

    def SQL_TEST_ITEM_RUN_RESULT_INSERT_QUERY(self, ttr_mt_id, ttr_test_item_name, ttr_test_item_result,
                                              ttr_test_item_remarks):
        # insert Qry (for insert  test data records)
        self.cursor = self.cnx.cursor()
        dt = datetime.date.today()
        insertQry = "INSERT INTO test_ti_results(ttr_mt_id,ttr_testitem_name,ttr_testitem_result,ttr_testitem_remarks) \
        VALUES (%d,%s,%s,%s)" % (ttr_mt_id, ttr_test_item_name, ttr_test_item_result, ttr_test_item_remarks)

        print
        insertQry
        self.cursor.execute(insertQry)
        self.cnx.commit()
        self.cursor.close()

    def SQL_UPDATE_QUERY(self, mt_result, mt_remark, mt_id):
        # UPDATE Qry (for updating main test run result & comments)
        self.cursor = self.cnx.cursor()

        insertQry = "UPDATE mst_test SET mt_result ='%s',mt_remark=%s WHERE mt_id = %s " \
                    % (mt_result, mt_remark, mt_id)
        print
        insertQry
        self.cursor.execute(insertQry)
        self.cnx.commit()
        self.cursor.close()

    def SQL_TEST_ITEM_RUN_RESULT_UPDATE_QUERY(self, mt_result, id):
        # UPDATE Qry (for updating main test run result & comments)
        self.cursor = self.cnx.cursor()

        insertQry = "UPDATE test_ti_results SET ttr_testitem_result =%s WHERE ttr_id = %s " \
                    % (mt_result, id)
        print
        insertQry
        self.cursor.execute(insertQry)
        self.cnx.commit()
        self.cursor.close()

    def SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(self, mt_result, id):
        # UPDATE Qry (for updating main test run result & comments)
        self.cursor = self.cnx.cursor()

        insertQry = "UPDATE test_detail_results SET td_res_param =%s WHERE td_id = %s " \
                    % (mt_result, id)
        print
        insertQry
        self.cursor.execute(insertQry)
        self.cnx.commit()
        self.cursor.close()

    def SQL_CUSTOMER_RECORD_INSERT_QUERY(self, mc_part_no, mc_config_ver, mc_cust_name):
        # insert Qry (for insert main test run records)
        self.cursor = self.cnx.cursor()
        dt = datetime.date.today()
        #     self.CustomerName=SQL_SELECT_QUERY(self,'mc_cust_name','mst_cust','mc_part_no',self.lineEdit_DUTPartNumber.text())
        #     self.ConfigVersion=SQL_SELECT_QUERY(self,'mc_config_ver','mst_cust','mc_part_no',self.lineEdit_DUTPartNumber.text())
        insertQry = "INSERT INTO mst_cust(mc_part_no,mc_config_ver,mc_cust_name)\
        VALUES ('%s','%s','%s')" % (mc_part_no, mc_config_ver, mc_cust_name)
        print
        insertQry
        self.cursor.execute(insertQry)
        self.cnx.commit()
        self.cursor.close()

    def SQL_CUSTOMER_RECORD_UPDATE_QUERY(self, part_number, config_version, customer_name):
        # UPDATE Qry (for updating main test run result & comments)

        self.cursor = self.cnx.cursor()

        insertQry = "UPDATE mst_cust SET mc_config_ver ='%s',mc_cust_name='%s' WHERE mc_part_no = '%s' " \
                    % (config_version, customer_name, part_number)
        print
        insertQry
        self.cursor.execute(insertQry)
        self.cnx.commit()
        self.cursor.close()

    def GENERIC_SQL_UPDATE_QUERY(self, tblName, updateColName, selColName, condition1, conditionValue1):
        # UPDATE Qry (for updating main test run result & comments)
        self.cursor = self.cnx.cursor()

        selectQry = "UPDATE  %s SET %s='%s' WHERE %s = %s \
               " % (tblName, updateColName, selColName, condition1, conditionValue1)
        print
        selectQry
        self.cursor.execute(selectQry)
        self.cnx.commit()
        self.cursor.close()

    def DELETE_TABLE_CONTENTS(self, table_name):

        self.cursor = self.cnx.cursor()
        insertQry = "TRUNCATE " + str(table_name)
        print
        insertQry
        self.cursor.execute(insertQry)
        self.cnx.commit()
        self.cursor.close()


def UPDATE_BULK_CUSTOMER_CONFIG_FILE_RECORD(Object):
    Object.DELETE_TABLE_CONTENTS('mst_cust')
    CUSTOMER_CONFIG_DATA_LIST = READ_CSV(f'{gui_global.files_directory_location}customer_detail.csv')

    for row in CUSTOMER_CONFIG_DATA_LIST:
        mc_part_no = row[0]
        mc_config_ver = row[1]
        mc_cust_name = row[2]
        Object.SQL_CUSTOMER_RECORD_INSERT_QUERY(mc_part_no, mc_config_ver, mc_cust_name)


# def ADD_COLUMN_TO_TABLE(tblName,addColName,afterColName):
#     self.cursor = self.cnx.cursor()
#
#     selectQry = "UPDATE  %s SET %s='%s' WHERE %s = %s \
#            " % (tblName,updateColName,selColName,condition1,conditionValue1)
#
#     selectQry = "ALTER TABLE %s ADD COLUMN %s VARCHAR(45) NULL DEFAULT NULL AFTER %s \
#            " % (tblName,addColName,afterColName)
#
#     print selectQry
#     self.cursor.execute(selectQry)
#     self.cnx.commit()


def READ_CSV(filename):
    with open(filename) as csvfile:

        reader = csv.DictReader(csvfile)
        # print reader
        ROW_LIST = []
        PARAMETER_LIST = []
        OID = []
        count_row = 0

        for row in reader:
            # print row
            count_row = count_row + 1
            ROW_LIST.append(row)
        ROW_LIST_LEN = len(ROW_LIST)
        # print ROW_LIST
        ROW = []
        ROW_2 = []
        for i in range(0, ROW_LIST_LEN):
            # print ROW_LIST[i]
            ROW.append([ROW_LIST[i]["PART NUMBER"], ROW_LIST[i]["CONFIG VERSION"], ROW_LIST[i]["CUSTOMER NAME"]])

        # print ROW

        return ROW


if __name__ == "__main__":

    float_voltage = 54.0
    # print READ_CSV('..\\files\\customer_detail.csv')
    # DELETE_TABLE_CONTENTS('mst_cust')
    #     print"connect "
    #     config_version='37'
    #     customer_name='BSNL'
    #     part_number='HE517417'
    #     print SQL_CUSTOMER_RECORD_UPDATE_QUERY(config_version,customer_name,part_number)
    # UPDATE_BULK_CUSTOMER_CONFIG_FILE_RECORD()

    while 1:
        sql = MY_SQL()

        id = sql.SQL_SELECT_2_QUERY('ttr_id', 'test_ti_results', 'ttr_mt_id', 400, 'ttr_testitem_name',
                                    'ATS_INITIALIZE')
        # SQL_SELECT_2_QUERY(ttr_testitem_result,test_ti_results,ttr_mt_id,50,ttr_testitem_name,'ATS_INITIALIZE')
        if id != 0:
            print("update row")
            SQL_TEST_ITEM_RUN_RESULT_UPDATE_QUERY(False, id)
        else:
            print("insert row")

        id = sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'UNIT_COMM', 'td_readby',
                                    'DCIF_COMM', 'td_mt_id', 400)
        print(id)

        if id != 0:
            print("update table")
            sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(False, id)
        else:
            print("insert table")



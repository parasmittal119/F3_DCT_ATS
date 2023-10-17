"""
Created on 18-08-2023

@author: paras.mittal
"""
## This file is the execution command list for Chroma AC Source 61511/12
##Following are the set of commands:
##0. Common
##1. System
##2. Instrument
##3. Fetch & Measure
##4. Output
##5. Source
##6. Configure
##7. Phase
##8. Status
##9. Trace
##10. List
##11. Pulse
##12. Step
##13. Synthesis
##14. Inter-harmonics
##15. Harmonics sense

## Common commands
## *IDN?
##*RST
# import sys
# sys.path.insert(0, '..\\')
import pyvisa
from ConfigFile import *

identify_unit = '*IDN?'
reset = '*RST'

## System commands
get_version = 'SYST:VERS?'
get_date = 'SYST:DATE?'
get_time = 'SYST:TIME?'

## Instrument commands
edit_all_phase = 'INST:EDIT ALL'
edit_each_phase = 'INST:EDIT EACH'
couple_all_phase = 'INST:COUP ALL'
couple_all_phase_none = 'INST:COUP NONE'
select_phase = 'INST:NSEL'
source_single_phase = 'INST:PHAS SINGLE'
source_three_phase = 'INST:PHAS THREE'
source_voltage_range_high = 'SOUR:VOLT:RANG HIGH'
source_voltage_range_low = 'SOUR:VOLT:RANG LOW'
source_ac_voltage_set = 'SOUR:VOLT:LEV:IMM:AMPL:AC'
source_ac_frequency_set = 'SOUR:FREQ:IMM'
output_ON = 'OUTP:STAT ON'
output_OFF = 'OUTP:STAT OFF'

## Fetch & Measure commands
read_ac_rms_current = 'MEAS:CURR:AC?'
read_ac_frequency = 'MEAS:FREQ?'
read_ac_rms_voltage = 'MEAS:VOLT:AC?'
read_ac_rms_voltage_LINE_V12 = 'MEAS:SCAL:LINE:V12?'
read_ac_rms_voltage_LINE_V23 = 'MEAS:LINE:V23?'
read_ac_rms_voltage_LINE_V31 = 'MEAS:LINE:V31?'
read_total_real_power = 'MEAS:POW:AC:TOT?'
read_total_apparent_power = 'MEAS:POW:AC:TOT:APP?'
read_pf = 'MEAS:POW:AC:PFAC?'

## Harmonics sense commands
set_mode_voltage_harmonics = 'SOUR:CONF:HARM:SOUR VOLT'
set_mode_current_harmonics = 'SOUR:CONF:HARM:SOUR CURR'
set_measurement_single_harmonics = 'SOUR:CONF:HARM:TIMES SINGLE'
set_measurement_continue_harmonics = 'SOUR:CONF:HARM:TIMES CONTINUE'
set_data_format_percent_harmonics = 'SOUR:CONF:HARM:PAR PERCENT'
set_data_format_value_harmonics = 'SOUR:CONF:HARM:PAR VALUE'
set_frequency_50_harmonics = 'SOUR:CONF:HARM:FREQ 50'
set_frequency_60_harmonics = 'SOUR:CONF:HARM:FREQ 60'
read_THD = 'MEAS:HARM:THD?'
read_harmonics_ON = 'SENS:HARM ON'
read_harmonics_OFF = 'SENS:HARM OFF'

## Distorted wave command set
set_waveform_buffer_A = 'SOUR:FUNC:SHAP A'
get_waveform_buffer_A = 'SOUR:FUNC:SHAP?'
set_distorted_waveform_1 = 'SOUR:FUNC:SHAP:A DST01'
set_distorted_waveform_2 = 'SOUR:FUNC:SHAP:A DST02'
set_distorted_waveform_3 = 'SOUR:FUNC:SHAP:A DST03'
set_distorted_waveform_4 = 'SOUR:FUNC:SHAP:A DST04'
set_distorted_waveform_5 = 'SOUR:FUNC:SHAP:A DST05'
set_distorted_waveform_6 = 'SOUR:FUNC:SHAP:A DST06'
set_distorted_waveform_7 = 'SOUR:FUNC:SHAP:A DST07'
set_distorted_waveform_8 = 'SOUR:FUNC:SHAP:A DST08'
set_distorted_waveform_9 = 'SOUR:FUNC:SHAP:A DST09'
set_distorted_waveform_10 = 'SOUR:FUNC:SHAP:A DST10'
set_distorted_waveform_11 = 'SOUR:FUNC:SHAP:A DST11'
set_distorted_waveform_12 = 'SOUR:FUNC:SHAP:A DST12'
set_distorted_waveform_13 = 'SOUR:FUNC:SHAP:A DST13'
set_distorted_waveform_14 = 'SOUR:FUNC:SHAP:A DST14'
set_distorted_waveform_15 = 'SOUR:FUNC:SHAP:A DST15'
set_distorted_waveform_16 = 'SOUR:FUNC:SHAP:A DST16'
set_distorted_waveform_17 = 'SOUR:FUNC:SHAP:A DST17'
set_distorted_waveform_18 = 'SOUR:FUNC:SHAP:A DST18'
set_distorted_waveform_19 = 'SOUR:FUNC:SHAP:A DST19'
set_distorted_waveform_20 = 'SOUR:FUNC:SHAP:A DST20'
set_distorted_waveform_21 = 'SOUR:FUNC:SHAP:A DST21'
set_distorted_waveform_22 = 'SOUR:FUNC:SHAP:A DST22'
set_distorted_waveform_23 = 'SOUR:FUNC:SHAP:A DST23'
set_distorted_waveform_24 = 'SOUR:FUNC:SHAP:A DST24'
set_distorted_waveform_25 = 'SOUR:FUNC:SHAP:A DST25'
set_distorted_waveform_26 = 'SOUR:FUNC:SHAP:A DST26'
set_distorted_waveform_27 = 'SOUR:FUNC:SHAP:A DST27'
set_distorted_waveform_28 = 'SOUR:FUNC:SHAP:A DST28'
set_distorted_waveform_29 = 'SOUR:FUNC:SHAP:A DST29'
set_distorted_waveform_30 = 'SOUR:FUNC:SHAP:A DST30'

get_distorted_waveform = 'SOUR:FUNC:SHAP:A?'

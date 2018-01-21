# gnss_status_viewer

GNSS quality viewer. Shows the current fix quality (e.g. RTK, FloatRTK, DGPS),
number of satellites observed, and the horizontal delusion of precision.


## Example

Here's what it looks like when running this program:

```
[INFO] [1516565360.176049, 1516434271.302132]: Number of satellites increased from 13 to 14
[INFO] [1516565360.176934, 1516434271.302132]: HDOP decreased from 0.82 to 0.8

[INFO] [1516565362.278148, 1516434273.404360]: Number of satellites decreased from 14 to 13
[INFO] [1516565362.278737, 1516434273.404360]: HDOP increased from 0.8 to 0.89

[INFO] [1516565362.480976, 1516434273.606435]: Fix quality changed from GPS to FloatRTK
[INFO] [1516565362.481327, 1516434273.606435]: Number of satellites decreased from 13 to 7
[INFO] [1516565362.481569, 1516434273.606435]: HDOP increased from 0.89 to 2.13

[INFO] [1516565366.578242, 1516434277.697674]: Fix quality changed from FloatRTK to RTK
[INFO] [1516565366.579443, 1516434277.697674]: Number of satellites decreased from 7 to 6
[INFO] [1516565366.580347, 1516434277.697674]: HDOP increased from 2.13 to 3.94

[INFO] [1516565366.778482, 1516434277.899627]: Fix quality changed from RTK to FloatRTK
[INFO] [1516565366.779559, 1516434277.899627]: Number of satellites increased from 6 to 7
[INFO] [1516565366.780447, 1516434277.899627]: HDOP decreased from 3.94 to 1.91

[INFO] [1516565366.877559, 1516434278.000723]: Fix quality changed from FloatRTK to RTK
[INFO] [1516565366.878753, 1516434278.000723]: HDOP increased from 1.91 to 2.6

[INFO] [1516565366.980365, 1516434278.101749]: HDOP decreased from 2.6 to 1.82

[INFO] [1516565367.079611, 1516434278.202733]: HDOP decreased from 1.82 to 1.8

Quality :       RTK
Num Sat :         7
HDOP    :       1.8

```


## License

MIT


## Author

Naoki Mizuno (mizuno.naoki@rm.is.tohoku.ac.jp)

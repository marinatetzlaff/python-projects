#An Analytical Detective
mvt = read.csv("mvtWeek1.csv")
max(mvt$ID)
min(mvt$Beat)


 mvt$Date[1]
 DateConvert = as.Date(strptime(mvt$Date, "%m/%d/%y %H:%M"))
 
 
 
 mvt$Month = months(DateConvert)
 mvt$Weekday = weekdays(DateConvert)
 mvt$Date = DateConvert
 
 table(mvt$Month)
 
 table(mvt$Weekday)
 
 table(mvt$Arrest,mvt$Month)
 
 hist(mvt$Date, breaks=100)
 
 boxplot(mvt$Date ~ mvt$Arrest)
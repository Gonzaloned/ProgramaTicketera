/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [dni]
      ,[num]
      ,[hora]
      ,[tipo]
      ,[atiende_nombre]
      ,[status]
  FROM [turnos].[dbo].[turnos_actual]

SELECT TOP (10) num FROM turnos_actual WHERE tipo=2 ORDER BY hora
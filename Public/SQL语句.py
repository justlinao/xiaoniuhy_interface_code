"""
����� Company ���н�ѡȡΨһ��ͬ��ֵ��������Ҫʹ�� SELECT DISTINCT ��䣺
SELECT DISTINCT Company FROM Orders

ORDER BY ���Ĭ�ϰ�������Լ�¼��������
�����ϣ�����ս���Լ�¼�������򣬿���ʹ�� DESC �ؼ��֡�
������ĸ˳����ʾ��˾���ƣ���������˳����ʾ˳��ţ�
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC, OrderNumber ASC

����Ҳ����ָ����Ҫ�������ݵ��У�
INSERT INTO table_name (��1, ��2,...) VALUES (ֵ1, ֵ2,....)

Update ��������޸ı��е����ݡ�
UPDATE ������ SET ������ = ��ֵ WHERE ������ = ĳֵ

DELETE �������ɾ�����е��С�
DELETE FROM ������ WHERE ������ = ֵ

ͨ��ʹ�� NOT �ؼ��֣����ǿ��Դ� "Persons" ����ѡȡ��ס�ڲ����� "lon" �ĳ�������ˣ�
SELECT * FROM Persons
WHERE City NOT LIKE '%lon%'   "%" �����ڶ���ͨ�����ģʽ��ȱ�ٵ���ĸ



"""
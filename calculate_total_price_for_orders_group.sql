DECLARE @id INT
SELECT @id=1; --тут меняется id для групп
 
WITH pr (row_id,parent_id,group_name) AS
 (SELECT row_id,parent_id,group_name FROM Orders WHERE row_id=@id
  UNION ALL
  SELECT Ord.row_id,Ord.parent_id,Ord.group_name
    FROM Orders Ord JOIN pr ON Ord.parent_id=pr.row_id) 
SELECT SUM(orI.price) 
  FROM pr JOIN OrderItems orI ON pr.row_id=orI.order_id
  WHERE pr.group_name IS NULL
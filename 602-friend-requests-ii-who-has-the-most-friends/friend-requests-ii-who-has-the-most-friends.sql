# Write your MySQL query statement below
with ids as(
    select requester_id as id from RequestAccepted
    union all
    select accepter_id from RequestAccepted
)
select id, count(*) as num from ids
group by id 
order by num desc
limit 1
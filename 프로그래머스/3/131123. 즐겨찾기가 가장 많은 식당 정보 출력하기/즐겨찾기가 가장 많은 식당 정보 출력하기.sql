SELECT r.FOOD_TYPE, r.REST_ID, r.REST_NAME, r.FAVORITES
FROM REST_INFO r
INNER JOIN (
    SELECT FOOD_TYPE, MAX(FAVORITES) AS MaxFavorites
    FROM REST_INFO
    GROUP BY FOOD_TYPE
) max_favorites ON r.FOOD_TYPE = max_favorites.FOOD_TYPE AND r.FAVORITES = max_favorites.MaxFavorites
ORDER BY r.FOOD_TYPE DESC;

from lasagna import (
    bake_time_remaining,
    preparation_time_in_minutes,
    elapsed_time_in_minutes,
)

LASAGNA_LAYERS = 3
ELAPSED_BAKING_TIME = 30

print(bake_time_remaining(ELAPSED_BAKING_TIME))
print(preparation_time_in_minutes(LASAGNA_LAYERS))
print(elapsed_time_in_minutes(LASAGNA_LAYERS, ELAPSED_BAKING_TIME))

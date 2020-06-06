# !/bin/bash
# pipenv install --dev

speedsurpries_path = "../speed-surprises/"

# run this script inside of tada diretory
default="pipenv run python tada_a_bigoh.py --directory $speedsurpries_path"

schema="--schema=../speed-surprises/speedsurprises/jsonschema/single_int_list.json"

modules=(
        lists.sorting
        search.basic_search
)

# functions and its expected time complexity should be matched in order
sort_funcs=(
          insertion_sort
          bubble_sort
          merge_sort
)

sort_timecomplexity_expectation=(
          O\(n\)
          O\(n^2\)
          O\(nlogn\)
)

search_funcs=(
          compute_linear_search
          compute_binary_search
)

search_timecomplexity_expectation=(
          O\(n\)
          O\(logn\)
)

# data generation strategies
list_sts=(
int_list
hypothesis\ $schema
)

# starting size options
startsize=(1 25 50 75 100 125 150 175 200 225 250 275 300)

# run sorting algorithm
run_sort () {
  # run each function
  for n in ${!sort_funcs[@]}; do
    # run each data generation strategy
    for ((i=0; i<${#list_sts[@]}; i++))
    do
      # run each starting size
      for size in ${startsize[@]}; do
        ${default} \
        --module speedsurprises.${modules[0]} \
        --function ${sort_funcs[n]} \
        --types ${list_sts[i]} \
        --startsize $size \
        --expect ${sort_timecomplexity_expectation[n]} \
        --steps 4
      done
    done
  done
}

# run searching algorithm
run_search () {
  for n in ${!search_funcs[@]}; do
    for ((i=0; i<${#list_sts[@]}; i++))
    do
      for size in ${startsize[@]}; do
        $default \
        --module speedsurprises.${modules[1]} \
        --function ${search_funcs[n]} \
        --types ${list_sts[i]} \
        --startsize $size \
        --expect ${search_timecomplexity_expectation[n]} \
        --steps 4
      done
    done
  done
}

# execute experiments
for ((i = 0 ; i <= 1 ; i++))
do
  run_sort
  run_search
done

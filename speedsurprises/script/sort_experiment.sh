# !/bin/bash
# chmod +x ./sort_experiment.sh
# pipenv install --dev

# run this script inside of tada diretory
speedsurprises_path="../speed-surprises/"

# default schema path
schema_path="${speedsurprises_path}speedsurprises/jsonschema/"

# default running command
run_command="pipenv run python tada_a_bigoh.py --directory ${speedsurprises_path}"

# path to the json schema
schema="${schema_path}single_int_list.json"

# starting size options
startsize=(1 25 50 75 100 125 150 175 200 225 250 275 300)

# step options (maximum rounds of each experiment)
steps=(5 10)

# modules to be run on
modules=(
        lists.sorting
)

# functions and its expected time complexity should be matched in order
funcs=(
          insertion_sort
          bubble_sort
          merge_sort
          python_sort
          wiggle_sort
          heap_sort
          quick_sort
          random_quick_sort
          intro_sort
)

expect_time_complexity=(
          O\(n\)
          O\(n^2\)
          O\(nlogn\)
          O\(nlogn\)
          O\(n\)
          O\(nlogn\)
          O\(n^2\)
          O\(n^2\)
          O\(nlogn\)
)


# run algorithm
run_experiment () {
  # run each function
  for n in ${!funcs[@]}; do
    # run each starting size
    for size in ${startsize[@]}; do
      # run each steps
      for step in ${steps[@]}; do
        ${run_command} \
        --module speedsurprises.${modules[0]} \
        --function ${funcs[n]} \
        --types hypothesis \
        --schema $schema \
        --startsize $size \
        --expect ${expect_time_complexity[n]} \
        --steps $step
      done
    done
  done
}

"""
A configuration file containing all the frequently changed settings

The user is encouraged to experiment by changing the settings in this 
file to try different neural network architectures and training settings.
"""

##############
# Versioning #
##############

# The name of the current version is gotten by "git describe".  
#  This determines the location and name of saved files

# If you want to continue training from a data generated by previous git version, 
# put the version history in this list (e.g. ['v1.0.2-r2', 'v1.0.2-r'])
prev_versions = [] # list most recent first

# the results are stored in this directory (in folders according to the "git describe" version)
results_dir = '../results/'

# use this for backwards compatibility with a previous version of this software
save_dir = '../save/'


############################
# Model (hyper-)parameters #
############################

# Model type (use the name of the class in models.py)
model_type = "ConvModel2D3D"

# How much history to use in the model.
# - If 1, then the model will only use the current state.
# - If 8, then the model will use the current state and the previous 7 states (if available)
prev_state_history = 1

# Whether to randomly rotate the input before calculating the neural network
# (There 48 color symmetries: 6 ways to rotate red face * 4 ways to rotate green face * 2 refections of yellow face = 48)
rotationally_randomize = True

# Whether to use a dictionary cache (with a max capacity) to speed up the neural network
use_cache = True if prev_state_history == 1 else False
max_cache_size = 10000

# kwargs for model
model_kwargs = \
    {"use_cache": use_cache,
     "max_cache_size": max_cache_size,
     "history": prev_state_history,
     "rotationally_randomize": rotationally_randomize}


#####################################
# Model Training (hyper-)parameters #
#####################################

# Validate the training data (once) to make sure it matches the current settings
validate_training_data = True

# Whether to augment training data with 48 color symmetries (see rotationally_randomize above)
augment_training_data = True

# How much data to use for training
prev_generations_used_for_training = 8
training_sample_ratio = 1/prev_generations_used_for_training

learning_rate = .001


###################################
# Self-Play (Training) parameters #
###################################

games_per_generation = 512
batch_size = 32

# training distance (how much to randomize the cube)
starting_distance = 1
min_distance = 1
win_rate_target = .5

# min/max number of games to play before stopping 
min_game_length = max(2, prev_state_history)
max_game_length = 100


#########################
# Evaluation parameters #
#########################

# Note: set both of these to 0 to skip the evaluation step

games_per_evaluation = 128
win_margin_to_become_best_model = 6


##################
# Multithreading #
##################

# This speeds up the training process by batching evaluations of the model (useful on CPU and GPU)
# It also allows the cpu and gpu to work at the same time
multithreaded = True


###################
# MCTS parameters #
###################

# Note: To use the model without MCTS, set
# - max_steps = 1
# - use_dirichet = None

# maximum exploration steps
max_steps = 1600

# exploration constant (c_puct)
# note: this is currently scaled by the value of the node because of the decay
exploration = 1.0

# decay (gamma)
# used for the value of the node, to measure both:
# - likelyhood of success (0 or >0) 
# - distance to the target (gamma ** distance)
decay = 0.95

# Dirichlet noise add to root node of MCTS to encourage exploration (default alpha is 1/12)
dirichlet_const = 1/12  # alpha (set to None if not using Dirichlet noise)

# maximum depth to explore (usually never reached)
max_depth = 900

# transposition table settings (usefule if history is 1)
use_transposition_table = True if prev_state_history == 1 else False
use_prebuilt_transposition_table = False # this setting is currently not used



   
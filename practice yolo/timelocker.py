from collections import Counter

def get_stable_class(predictions_list):
    counts = Counter(predictions_list)
    
    majority_class = counts.most_common(1)[0][0]
    
    return majority_class

frame_history = [1, 1, 0, 1, 1]

final_decision = get_stable_class(frame_history)

if final_decision == 1:
    print("Final decision: Accident(confirmed by majority vote)")
else:
    print("Final decision: Car")

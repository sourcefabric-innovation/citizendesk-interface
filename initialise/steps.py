from main import Init, init_collection

init_steps = Init('coverages', [{
    'description': 'I have contacted this citizen reporter',
    'mandatory': False
}, {
    'description': 'I have obtained the rights to use this report from the citizen reporter',
    'mandatory': False
}, {
    'description': 'I have determined the location of the report',
    'mandatory': False
}, {
}])

if __name__ == "__main__": init_collection(init_steps)

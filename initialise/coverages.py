from uuid import uuid4

from main import Init, init_collection

init_coverages = Init('coverages', [{
    'title': 'default coverage',
    'uuid': str(uuid4().hex) # keep this in synch with the entity
}])

if __name__ == "__main__": init_collection(init_coverages)

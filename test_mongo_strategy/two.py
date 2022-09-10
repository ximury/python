from pymongo import UpdateOne

li = [
    UpdateOne(
        {'_id': '67c3f453fc344b6e968cf9d1f8500acd'},
        {'$set': {'_id': '67c3f453fc344b6e968cf9d1f8500acd', 'yes': True}}
    )
]

li.append(    UpdateOne(
        {'_id': '67c3f453fc344b6e968cf9d1f8500acd'},
        {'$set': {'_id': '67c3f453fc344b6e968cf9d1f8500acd', 'yes': False}}
    ))

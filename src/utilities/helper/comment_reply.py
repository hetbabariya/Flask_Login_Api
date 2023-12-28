from flask import jsonify
from src.utilities.helper.get_comment_by_id import get_comment_by_id
from src.database.model.comment_reply import PostCommentReply
from schemaObj import post_comment_reply_response_schema

def create_comment_reply(comment_id , comment_reply , user_id , db):

    comment_data = get_comment_by_id(comment_id=comment_id)
    new_comment_reply = PostCommentReply(comment_reply = comment_reply , comment_id = comment_id ,user_id = user_id , post_id = comment_data.post_id)
    
    db.session.add(new_comment_reply)
    db.session.commit()

    comment_data.comment_reply_count += 1
    db.session.commit()     

    return post_comment_reply_response_schema.dump(new_comment_reply)




     
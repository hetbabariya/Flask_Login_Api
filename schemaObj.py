from src.database.schema.schema import UserResponse , UserRequest , UserForgrtPwd , UserChangePwd
from src.database.schema.post import CreatePost , UpdatePost , ResponsePost
from src.database.schema.post_like import PostLikeSchema , PostLikeResponse
from src.database.schema.post_comment import PostCommentSchema , PostCommentUpdateSchema , PostCommentResponseSchema , PostRequestForCommentUser , PostCommentDelRequest
from src.database.schema.post_comment_reply import PostCommentReplySchema , PostCommentReplyUpdateSchema , PostCommentReplyResponseSchema , PostCommentRemoveRequest
from src.database.schema.comemnt_and_reply_like import commentLikeRequestSchema , commentLikeResponseSchema , commmentReplyLikeRequestSchema  , commentLikeDelete


user_response = UserResponse(many=True)
user_response_single = UserResponse()
user_request = UserRequest()
User_forgrt_pwd = UserForgrtPwd()
user_change_pwd = UserChangePwd()
create_post = CreatePost()
update_post = UpdatePost()
post_response = ResponsePost()
post_response_all = ResponsePost(many=True)
post_like = PostLikeSchema()
post_comment_schema = PostCommentSchema()
post_comment_update_schema = PostCommentUpdateSchema()
post_comment_response_schema = PostCommentResponseSchema()
post_comment_all_user_response_schema = PostCommentResponseSchema(many=True)
Post_like_all_user_response_schema = PostLikeResponse(many=True)
post_id_rquest_schema = PostRequestForCommentUser()
post_comment_reply_schema = PostCommentReplySchema()
post_comment_reply_update_schema = PostCommentReplyUpdateSchema()
post_comment_reply_response_schema = PostCommentReplyResponseSchema()
post_comment_like_request_schema = commentLikeRequestSchema()
post_comment_reply_like_request_schema = commmentReplyLikeRequestSchema()
post_comment_like_response_schema = commentLikeResponseSchema()
post_comment_delete_request = PostCommentDelRequest()
post_comment_reply_delete_request = PostCommentRemoveRequest()
post_comment_like_delete_request = commentLikeDelete()
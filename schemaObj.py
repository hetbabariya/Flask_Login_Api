from src.database.schema.schema import UserResponse , UserRequest , UserForgrtPwd , UserChangePwd
from src.database.schema.post import CreatePost , UpdatePost , ResponsePost
from src.database.schema.post_like import PostLikeSchema , PostLikeResponse
from src.database.schema.post_comment import PostCommentSchema , PostCommentUpdateSchema , PostCommentResponseSchema , PostRequestForCommentUser


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

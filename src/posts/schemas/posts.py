from typing import Optional

from ninja import ModelSchema, Schema
from ninja_schema import model_validator
from pydantic import field_validator

from posts.models import MAX_TITLE_LENGTH, MIN_TITLE_LENGTH, Post
from posts.schemas.general import AuthorSchema


class AutoReplyConfigSchemaCreate(Schema):
    delay_secs: int = 0

    @field_validator("delay_secs")
    def delay_secs_not_negative(cls, v):
        if v < 0:
            raise ValueError("Delay must be a positive integer")
        return v


class PostOutSchema(ModelSchema):
    id: int
    author: AuthorSchema

    class Meta:
        model = Post
        fields = "__all__"


class PostUpdateSchema(ModelSchema):

    class Meta:
        model = Post
        exclude = ["id", "author", "created_at", "updated_at", "is_blocked"]


class PostCreateSchema(ModelSchema):
    auto_reply_config: Optional[AutoReplyConfigSchemaCreate] = None

    @model_validator("title", check_fields=False)
    def title_length(cls, v):
        if len(v) < MIN_TITLE_LENGTH or len(v) > MAX_TITLE_LENGTH:
            raise ValueError(f"Title must be between {MIN_TITLE_LENGTH} and {MAX_TITLE_LENGTH} characters")
        return v

    @model_validator("content", check_fields=False)
    def content_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Content cannot be empty")
        return v

    class Meta:
        model = Post
        fields = ["title", "content"]

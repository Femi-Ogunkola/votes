from fastapi import APIRouter
from fastapi import Body
from fastapi.encoders import jsonable_encoder
from server.database import delete_poll_option
from server.database import update_poll_option_name
from server.database import vote_poll

from server.database import add_poll
from server.database import delete_poll
from server.database import retrieve_poll
from server.database import retrieve_polls
from server.database import update_poll
from server.models.poll import ErrorResponseModel
from server.models.poll import PollSchema
from server.models.poll import ResponseModel
from server.models.poll import UpdatePollModel

router = APIRouter()

@router.post("/", response_description="poll data added into the database")
async def add_poll_data(poll: PollSchema = Body(...)):
    poll = jsonable_encoder(poll)
    new_poll = await add_poll(poll)
    return ResponseModel(new_poll, "poll added successfully.")

@router.get("/", response_description="poll retrieved")
async def get_polls():
    polls = await retrieve_polls()
    if polls:
        return ResponseModel(polls, "polls data retrieved successfully")
    return ResponseModel(polls, "Empty list returned")


@router.get("/{id}", response_description="poll data retrieved")
async def get_poll_data(id):
    poll = await retrieve_poll(id)
    if poll:
        return ResponseModel(poll, "poll data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "poll doesn't exist.")

@router.put("/{id}")
async def update_poll_data(id: str, req: UpdatePollModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_poll = await update_poll(id, req)
    if updated_poll:
        return ResponseModel(
            "poll with ID: {} name update is successful".format(id),
            "poll name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the poll data.",
    )

@router.put("/id/{id}/update-option-name")
async def update_poll_option(id: str, optionName: list = Body(...)):
    updated_poll = await update_poll_option_name(id, {"optionNames": optionName})
    if updated_poll:
        return ResponseModel(
            "poll with ID: {} option update is successful".format(id),
            "poll option updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the poll data.",
    )

@router.put("/id/{id}/delete-option")
async def update_poll_option(id: str, optionName: str = Body(...)):
    updated_poll = await delete_poll_option(id, optionName)
    if updated_poll:
        return ResponseModel(
            "poll with ID: {} option update is successful".format(id),
            "poll option updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the poll data.",
    )

@router.put("/{userId}/id/{pollId}/vote")
async def vote_poll_option(pollId: str, userId: str, option: str = Body(...)):
    # option = f'option.{option}'
    voted_poll = await vote_poll(pollId, userId,{"vote": option})
    if voted_poll:
        return ResponseModel(
            f"poll with ID: {pollId} vote update is successful",
            "poll vote updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the poll data.",
    )

@router.delete("/{id}", response_description="poll data deleted from the database")
async def delete_poll_data(id: str):
    deleted_poll = await delete_poll(id)
    if deleted_poll:
        return ResponseModel(
            "poll with ID: {} removed".format(id), "poll deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "poll with id {0} doesn't exist".format(id)
    )

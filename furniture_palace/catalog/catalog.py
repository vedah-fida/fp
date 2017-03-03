import datetime
from accounts.models import TempCarpenter
from catalog.models import LentTool, Tool


def get_lent_tools_record():
    lent_tools = LentTool.objects.all()
    return lent_tools


def get_returned_lent_tools():
    lent_tools = LentTool.objects.all().filter(returned=True)
    return lent_tools


def get_lent_tools():
    lent_tools = LentTool.objects.all().filter(returned=None)
    return lent_tools


def get_lent_tool(lent_tool_id):
    lent_tool = LentTool.objects.get(id=lent_tool_id)
    return lent_tool


def lend_tool(tool_id, temp_carpenter_id):
    tool = Tool.objects.get(id=tool_id)
    temp_carpenter = TempCarpenter.objects.get(id=temp_carpenter_id)

    new_lent_tool = LentTool()
    new_lent_tool.tool = tool
    new_lent_tool.temp_carpenter = temp_carpenter

    new_lent_tool.save()


def update_lent_tool_with(lend_id, damaged_status, returned_status):
    lent_tool = LentTool.objects.get(id=lend_id)
    now = datetime.datetime.now().date()
    lent_days = abs((lent_tool.lend_date - datetime.datetime.now().date()).days)
    if lent_days == 0:
        lent_days = 1
        lending_fee = lent_tool.tool.lending_rate_per_day * lent_days
    else:
        lending_fee = lent_tool.tool.lending_rate_per_day * lent_days

    lent_tool.return_date = now
    lent_tool.days_with_tool = lent_days
    lent_tool.lending_fee = lending_fee
    lent_tool.was_damaged = damaged_status
    lent_tool.returned = returned_status
    lent_tool.save()


from PyQt5.QtWidgets import QApplication

import idaapi
import idautils
import idc


# from: https://github.com/igogo-x86/HexRaysPyTools
class ActionManager(object):
    def __init__(self):
        self.__actions = []

    def register(self, action):
        self.__actions.append(action)
        idaapi.register_action(
            idaapi.action_desc_t(action.name, action.description, action, action.hotkey)
        )

    def initialize(self):
        pass

    def finalize(self):
        for action in self.__actions:
            idaapi.unregister_action(action.name)


action_manager = ActionManager()


# visited = set()

def collect_function_pseudocode(func_ea, visited):
    if func_ea in visited:
        return ""
    visited.add(func_ea)

    cfunc = idaapi.decompile(func_ea)
    if not cfunc:
        return "Cannot decompile function at 0x{:X}\n".format(func_ea)

    code_str = ""
    code_str += "=================================================\n"
    code_str += "Function at 0x{:X}:\n".format(func_ea)
    code_str += str(cfunc)  
    code_str += "\n=================================================\n\n"

    func_obj = idaapi.get_func(func_ea)
    if not func_obj:
        return code_str

    flowchart = idaapi.FlowChart(func_obj)
    for block in flowchart:
        for head in idautils.Heads(block.start_ea, block.end_ea):
            # print(f"head: 0x{hex(head)}")
            # 使用 IDA 提供的API判断是否是函数调用指令（多架构通用）
            if idaapi.is_call_insn(head) or idaapi.ua_mnem(head) == "B":
                # print(f"is call")
                call_target = idc.get_operand_value(head, 0)
                # 如果IDA能够识别call目标并确定它在函数列表里
                if call_target and idaapi.get_func(call_target):
                    code_str += collect_function_pseudocode(call_target, visited)

    return code_str

class Action(idaapi.action_handler_t):
    """
    Convenience wrapper with name property allowing to be registered in IDA using ActionManager
    """
    description = None
    hotkey = None

    def __init__(self):
        super(Action, self).__init__()

    @property
    def name(self):
        return "collect_function_pseudocode:" + type(self).__name__

    def activate(self, ctx):
        # type: (idaapi.action_activation_ctx_t) -> None
        raise NotImplementedError

    def update(self, ctx):
        # type: (idaapi.action_activation_ctx_t) -> None
        raise NotImplementedError



class CFPMenuAction(Action):
    TopDescription = "collect_function_pseudocode"

    def __init__(self):
        super(CFPMenuAction, self).__init__()

    def activate(self, ctx) -> None:
        raise NotImplemented

    def update(self, ctx) -> None:
        if ctx.form_type == idaapi.BWN_FUNCS or ctx.form_type == idaapi.BWN_PSEUDOCODE or ctx.form_type == idaapi.BWN_DISASM:
            idaapi.attach_action_to_popup(ctx.widget, None, self.name, self.TopDescription + "/")
            return idaapi.AST_ENABLE_FOR_WIDGET
        return idaapi.AST_DISABLE_FOR_WIDGET


class GenerateFuncCode(CFPMenuAction):
    description = "Generate Func Code on current func"

    def __init__(self):
        super(GenerateFuncCode, self).__init__()

    def activate(self, ctx):
        main()


def main():
    start_ea = idc.here()
    func = idaapi.get_func(start_ea)
    if not func:
        print("No function found at 0x{:X}".format(start_ea))
        return
    full_code = collect_function_pseudocode(func.start_ea, visited=set())
    print(full_code)
    try:
        QApplication.clipboard().setText(full_code)
        print("The generated func code has been copied to the clipboard!")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

action_manager.register(GenerateFuncCode())



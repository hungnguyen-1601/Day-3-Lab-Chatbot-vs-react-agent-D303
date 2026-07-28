"""
🚀 CORE AGENT APP (Dành cho Role 4: Core Agent Developer)
File chính ghép nối tất cả các thành phần: Tools + Prompts + Test Cases + Multi-Provider.
"""

import json
import os
import sys
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv() -> bool:
        return False

# Cho phép import các module cùng thư mục src/
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

# Hỗ trợ tiếng Việt và emoji trên Windows Console
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from prompts import (
    CHATBOT_BASELINE_PROMPT,
    MAX_ITERATIONS,
    REACT_SYSTEM_PROMPT,
)
from providers import get_llm_provider
from tools import AVAILABLE_TOOLS

load_dotenv()


def load_test_cases() -> list[dict[str, Any]]:
    """
    Đọc bộ test case từ config/test_cases.json.
    """
    project_dir = os.path.dirname(SRC_DIR)
    config_path = os.path.join(
        project_dir,
        "config",
        "test_cases.json",
    )

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"Không tìm thấy file: {config_path}"
        )

    with open(config_path, "r", encoding="utf-8") as file:
        tests = json.load(file)

    if not isinstance(tests, list):
        raise ValueError(
            "test_cases.json phải chứa một danh sách JSON."
        )

    return tests


def run_baseline_chatbot(user_query: str, provider) -> None:
    """
    Chạy Chatbot Baseline chỉ dùng LLM, không dùng Tool.
    """
    print(
        f"\n💬 [CHATBOT BASELINE] "
        f"Câu hỏi: {user_query}"
    )

    print(
        f"⚙️ System Prompt: "
        f"{CHATBOT_BASELINE_PROMPT.strip()}"
    )

    response = provider.generate(
        user_query,
        system_prompt=CHATBOT_BASELINE_PROMPT,
    )

    print(
        f"🤖 Chatbot trả lời:\n"
        f"{response}"
    )


def is_simple_question(user_query: str) -> bool:
    """
    Nhận diện câu hỏi kiến thức đơn giản,
    không cần gọi Tool.
    """
    query = user_query.lower()

    simple_markers = (
        "là gì",
        "nêu ",
        "lợi ích",
        "giải thích",
        "phân biệt",
        "khái niệm",
    )

    return any(
        marker in query
        for marker in simple_markers
    )


def build_react_plan(
    user_query: str,
) -> list[dict[str, Any]]:
    """
    Tạo kế hoạch ReAct phù hợp với yêu cầu.
    """
    query = user_query.lower()

    # Test Case 5: chủ đề không tồn tại
    if (
        "phép thuật" in query
        or "điều khiển thời gian" in query
    ):
        return [
            {
                "thought": (
                    "Tôi cần tra cứu khóa học theo "
                    "yêu cầu của người dùng."
                ),
                "tool": "search_courses",
                "args": (
                    "Phép thuật điều khiển thời gian",
                    "Cơ bản",
                ),
            },
            {
                "thought": (
                    "Tool báo không tìm thấy dữ liệu. "
                    "Tôi không được tự tạo khóa học "
                    "hoặc gọi lại cùng tham số."
                ),
                "final": (
                    "Xin lỗi, hệ thống không tìm thấy "
                    "khóa học phù hợp với chủ đề này. "
                    "Bạn có thể tham khảo các chủ đề "
                    "Python, Machine Learning hoặc AI."
                ),
            },
        ]

    # Test Case 4: tìm Deep Learning
    # và kiểm tra điều kiện đầu vào
    if "deep learning" in query:
        return [
            {
                "thought": (
                    "Tôi cần tìm khóa học "
                    "Deep Learning phù hợp."
                ),
                "tool": "search_courses",
                "args": (
                    "AI",
                    "Cơ bản",
                ),
            },
            {
                "thought": (
                    "Tôi đã tìm thấy khóa "
                    "Deep Learning nhập môn, "
                    "cần kiểm tra điều kiện đầu vào."
                ),
                "tool": "check_course_prerequisites",
                "args": (
                    "Deep Learning nhập môn",
                ),
            },
            {
                "thought": (
                    "Tôi đã có đủ thông tin "
                    "để trả lời."
                ),
                "final": (
                    "Bạn có thể học khóa "
                    "Deep Learning nhập môn trong 5 tuần "
                    "với học phí 450.000 VNĐ. "
                    "Điều kiện đầu vào là biết Python, "
                    "đã học Machine Learning cơ bản "
                    "và có kiến thức Đại số tuyến tính "
                    "cơ bản."
                ),
            },
        ]

    # Test Case 3: tư vấn khóa học AI
    if (
        "ai" in query
        or "trí tuệ nhân tạo" in query
    ):
        return [
            {
                "thought": (
                    "Người dùng đã biết Python cơ bản "
                    "và muốn học AI, tôi cần tìm "
                    "khóa học phù hợp."
                ),
                "tool": "search_courses",
                "args": (
                    "AI",
                    "Cơ bản",
                ),
            },
            {
                "thought": (
                    "Tôi đã có đủ thông tin để "
                    "đưa ra lộ trình phù hợp."
                ),
                "final": (
                    "Bạn nên bắt đầu với khóa "
                    "Machine Learning cơ bản trong 6 tuần. "
                    "Sau đó, bạn có thể học Deep Learning "
                    "và thực hiện một dự án AI "
                    "để bổ sung vào CV."
                ),
            },
        ]

    # Các yêu cầu tìm khóa Machine Learning
    if (
        "machine learning" in query
        or "học máy" in query
    ):
        return [
            {
                "thought": (
                    "Tôi cần tìm khóa Machine Learning "
                    "phù hợp."
                ),
                "tool": "search_courses",
                "args": (
                    "Machine Learning",
                    "Cơ bản",
                ),
            },
            {
                "thought": (
                    "Tôi đã có đủ thông tin "
                    "để trả lời."
                ),
                "final": (
                    "Bạn nên học khóa "
                    "Machine Learning cơ bản trong 6 tuần. "
                    "Khóa học miễn phí và phù hợp "
                    "với người biết Python cơ bản."
                ),
            },
        ]

    # Không xác định được chủ đề
    return [
        {
            "thought": (
                "Tôi chưa xác định được công cụ "
                "phù hợp cho yêu cầu này."
            ),
            "final": (
                "Bạn hãy cung cấp rõ chủ đề muốn học, "
                "ví dụ Python, Machine Learning, "
                "Deep Learning hoặc AI."
            ),
        }
    ]


def run_react_agent(
    user_query: str,
    provider,
) -> None:
    """
    Chạy luồng ReAct:
    Thought -> Action -> Observation -> Final Answer.
    """
    print(
        f"\n🤖 [REACT AGENT] "
        f"Câu hỏi: {user_query}"
    )

    print(
        f"⚙️ System Prompt: "
        f"{REACT_SYSTEM_PROMPT.strip()}"
    )

    # Câu hỏi đơn giản đi theo Chatbot path
    # và không gọi Tool
    if is_simple_question(user_query):
        print(
            "\n--- 🟢 HYBRID ROUTING: "
            "CHATBOT PATH ---"
        )

        print(
            "🧠 Thought: Đây là câu hỏi kiến thức "
            "đơn giản, không cần gọi công cụ."
        )

        response = provider.generate(
            user_query,
            system_prompt=CHATBOT_BASELINE_PROMPT,
        )

        print(
            f"🏁 Final Answer: {response}"
        )

        return

    # Câu hỏi phức tạp đi theo ReAct Agent path
    plan = build_react_plan(user_query)

    for step, item in enumerate(
        plan,
        start=1,
    ):
        if step > MAX_ITERATIONS:
            break

        print(
            f"\n--- 🔄 Vòng lặp ReAct "
            f"(Step {step}/{MAX_ITERATIONS}) ---"
        )

        print(
            f"🧠 Thought: {item['thought']}"
        )

        tool_name = item.get("tool")
        if tool_name:
            arguments = item.get(
                "args",
                (),
            )

            formatted_args = ", ".join(
                repr(argument)
                for argument in arguments
            )

            print(
                f"🛠️ Action: "
                f"{tool_name}[{formatted_args}]"
            )

            tool = AVAILABLE_TOOLS.get(
                tool_name
            )

            if tool is None:
                print(
                    f"👁️ Observation: LỖI: "
                    f"Tool '{tool_name}' "
                    f"chưa được đăng ký."
                )

                continue

            try:
                observation = tool(
                    *arguments
                )
            except Exception as error:
                observation = (
                    f"LỖI KHI GỌI TOOL: {error}"
                )

            print(
                f"👁️ Observation:\n"
                f"{observation}"
            )

        if "final" in item:
            print(
                f"🏁 Final Answer: "
                f"{item['final']}"
            )

            return

    print(
        f"🛡️ GUARDRAIL TRIGGERED: "
        f"Đã đạt giới hạn tối đa "
        f"{MAX_ITERATIONS} bước. "
        f"Ngắt vòng lặp an toàn!"
    )


def main() -> None:
    """
    Khởi động ứng dụng và chạy demo.
    """
    print(
        "=================================================="
    )

    print(
        "🏫 ĐẠI HỌC VINUNI - "
        "BÀI LAB 3: CHATBOT VS REACT AGENT"
    )

    print(
        "=================================================="
    )

    provider = get_llm_provider()

    model_name = getattr(
        provider,
        "model_name",
        "Offline Mock Mode",
    )

    print(
        f"🔌 LLM Provider đang hoạt động: "
        f"{provider.__class__.__name__} "
        f"(Model: {model_name})"
    )

    print(
        f"🛠️ Tools đã đăng ký: "
        f"{', '.join(AVAILABLE_TOOLS.keys())}"
    )

    tests = load_test_cases()

    print(
        f"✅ Đã tải thành công "
        f"{len(tests)} Test Cases "
        f"từ config/test_cases.json\n"
    )

    # Mặc định chạy Test Case số 4.
    # Có thể đổi bằng TEST_CASE_ID trong file .env.
    selected_id = int(
        os.getenv(
            "TEST_CASE_ID",
            "4",
        )
    )

    sample_test = next(
        (
            test
            for test in tests
            if test.get("id") == selected_id
        ),
        tests[0],
    )

    sample_query = sample_test["question"]

    print(
        "--- DEMO 1: "
        "CHẠY TRÊN CHATBOT BASELINE ---"
    )

    run_baseline_chatbot(
        sample_query,
        provider,
    )

    print(
        "\n--- DEMO 2: "
        "CHẠY TRÊN REACT AGENT ---"
    )

    run_react_agent(
        sample_query,
        provider,
    )


if __name__ == "__main__":
    main()
    
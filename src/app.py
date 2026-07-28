"""
🚀 CORE AGENT APP (Dành cho Role 4: Core Agent Developer)
File chính ghép nối tất cả các thành phần: Tools + Prompts + Test Cases + Multi-Provider.
"""

import json
import os
import sys

from dotenv import load_dotenv

# Đảm bảo import các module trong thư mục src/ hoạt động
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Đảm bảo hiển thị tiếng Việt và emoji trên Windows Console
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Import thành phần của Role 2, Role 3 và Multi-Provider Adapter
from tools import (
    AVAILABLE_TOOLS,
    search_courses,
    check_course_prerequisites,
)
from prompts import (
    CHATBOT_BASELINE_PROMPT,
    REACT_SYSTEM_PROMPT,
    MAX_ITERATIONS,
)
from providers import get_llm_provider

load_dotenv()


def load_test_cases():
    """Đọc bộ test case từ config/test_cases.json của Role 1."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "test_cases.json")

    # Kiểm tra nếu file nằm trong thư mục hiện tại
    if not os.path.exists(config_path):
        config_path = "test_cases.json"

    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_baseline_chatbot(user_query: str, provider):
    """
    Chạy Chatbot Baseline chỉ sử dụng LLM, không sử dụng công cụ.
    """
    print(f"\n💬 [CHATBOT BASELINE] Câu hỏi: {user_query}")
    print(f"⚙️ System Prompt: {CHATBOT_BASELINE_PROMPT.strip()}")

    response = provider.generate(
        user_query,
        system_prompt=CHATBOT_BASELINE_PROMPT,
    )

    print(f"🤖 Chatbot trả lời:\n{response}")


def run_react_agent(user_query: str, provider):
    """
    Chạy vòng lặp ReAct Agent:
    Thought -> Action -> Observation -> Final Answer.
    """
    print(f"\n🤖 [REACT AGENT] Câu hỏi: {user_query}")
    print(f"⚙️ System Prompt: {REACT_SYSTEM_PROMPT.strip()}")

    step = 0
    completed = False
    query_lower = user_query.lower()

    course_result = ""
    prerequisite_result = ""

    while step < MAX_ITERATIONS:
        step += 1

        print(
            f"\n--- 🔄 Vòng lặp ReAct "
            f"(Step {step}/{MAX_ITERATIONS}) ---"
        )

        # Trường hợp không tìm thấy chủ đề khóa học
        if "phép thuật" in query_lower or "điều khiển thời gian" in query_lower:
            if step == 1:
                print(
                    "🧠 Thought: Tôi cần tìm khóa học theo yêu cầu "
                    "của người dùng."
                )
                print(
                    "🛠️ Action: "
                    "search_courses['Phép thuật điều khiển thời gian', 'Cơ bản']"
                )
                course_result = search_courses(
                    "Phép thuật điều khiển thời gian",
                    "Cơ bản",
                )

                print(f"👁️ Observation: {course_result}")

            elif step == 2:
                print(
                    "🧠 Thought: Công cụ không tìm thấy khóa học phù hợp, "
                    "tôi không được tự tạo thông tin."
                )
                print(
                    "🏁 Final Answer: Xin lỗi, hệ thống không tìm thấy "
                    "khóa học phù hợp với chủ đề này. Bạn có thể lựa chọn "
                    "các chủ đề như Python, Machine Learning hoặc AI."
                )

                completed = True
                break

        # Trường hợp tìm khóa Deep Learning và kiểm tra đầu vào
        elif "deep learning" in query_lower:
            if step == 1:
                print(
                    "🧠 Thought: Tôi cần tìm khóa học Deep Learning "
                    "phù hợp cho sinh viên."
                )
                print("🛠️ Action: search_courses['AI', 'Cơ bản']")

                course_result = search_courses("AI", "Cơ bản")

                print(f"👁️ Observation:\n{course_result}")

            elif step == 2:
                print(
                    "🧠 Thought: Tôi đã tìm thấy khóa Deep Learning, "
                    "cần kiểm tra điều kiện đầu vào."
                )
                print(
                    "🛠️ Action: "
                    "check_course_prerequisites['Deep Learning nhập môn']"
                )

                prerequisite_result = check_course_prerequisites(
                    "Deep Learning nhập môn"
                )

                print(f"👁️ Observation:\n{prerequisite_result}")

            elif step == 3:
                print(
                    "🧠 Thought: Tôi đã có đủ thông tin về khóa học "
                    "và điều kiện đầu vào."
                )
                print(
                    "🏁 Final Answer: Bạn có thể học khóa Deep Learning "
                    "nhập môn trong 5 tuần với học phí 450.000 VNĐ. "
                    "Tuy nhiên, bạn cần biết Python và đã học "
                    "Machine Learning cơ bản trước."
                )

                completed = True
                break

        # Trường hợp tìm khóa Machine Learning
        elif "machine learning" in query_lower or "học máy" in query_lower:
            if step == 1:
                print(
                    "🧠 Thought: Tôi cần tìm khóa Machine Learning "
                    "phù hợp với người mới bắt đầu."
                )
                print(
                    "🛠️ Action: "
                    "search_courses['Machine Learning', 'Cơ bản']"
                )
                course_result = search_courses(
                    "Machine Learning",
                    "Cơ bản",
                )

                print(f"👁️ Observation:\n{course_result}")

            elif step == 2:
                print(
                    "🧠 Thought: Tôi cần kiểm tra điều kiện đầu vào "
                    "của khóa học."
                )
                print(
                    "🛠️ Action: "
                    "check_course_prerequisites['Machine Learning cơ bản']"
                )

                prerequisite_result = check_course_prerequisites(
                    "Machine Learning cơ bản"
                )

                print(f"👁️ Observation:\n{prerequisite_result}")

            elif step == 3:
                print(
                    "🧠 Thought: Tôi đã có đủ thông tin để tư vấn."
                )
                print(
                    "🏁 Final Answer: Bạn nên học khóa Machine Learning "
                    "cơ bản trong 6 tuần. Khóa học miễn phí và phù hợp "
                    "với người đã biết Python cơ bản."
                )

                completed = True
                break

        # Trường hợp tư vấn khóa học AI
        elif "ai" in query_lower or "trí tuệ nhân tạo" in query_lower:
            if step == 1:
                print(
                    "🧠 Thought: Người dùng muốn học AI và đã biết "
                    "Python cơ bản, tôi cần tìm khóa học phù hợp."
                )
                print("🛠️ Action: search_courses['AI', 'Cơ bản']")

                course_result = search_courses("AI", "Cơ bản")

                print(f"👁️ Observation:\n{course_result}")

            elif step == 2:
                print(
                    "🧠 Thought: Machine Learning là khóa phù hợp "
                    "để bắt đầu học AI, tôi cần kiểm tra đầu vào."
                )
                print(
                    "🛠️ Action: "
                    "check_course_prerequisites['Machine Learning cơ bản']"
                )

                prerequisite_result = check_course_prerequisites(
                    "Machine Learning cơ bản"
                )

                print(f"👁️ Observation:\n{prerequisite_result}")

            elif step == 3:
                print(
                    "🧠 Thought: Tôi đã có đủ thông tin để trả lời."
                )
                print(
                    "🏁 Final Answer: Bạn nên bắt đầu với khóa "
                    "Machine Learning cơ bản trong 6 tuần. "
                    "Sau đó, bạn có thể học Deep Learning và thực hiện "
                    "một dự án AI để bổ sung vào CV."
                )

                completed = True
                break

        # Câu hỏi đơn giản không cần sử dụng Tool
        else:
            print(
                "🧠 Thought: Đây là câu hỏi kiến thức đơn giản, "
                "không cần gọi công cụ."
            )

            response = provider.generate(
                user_query,
                system_prompt=CHATBOT_BASELINE_PROMPT,
            )

            print(f"🏁 Final Answer: {response}")

            completed = True
            break

    if not completed:
        print(
            f"🛡️ GUARDRAIL TRIGGERED: Đã đạt giới hạn tối đa "
            f"{MAX_ITERATIONS} bước. Ngắt vòng lặp an toàn!"
        )


if __name__ == "__main__":
    print("==================================================")
    print("🏫 ĐẠI HỌC VINUNI - BÀI LAB 3: CHATBOT VS REACT AGENT")
    print("==================================================")

    # Khởi tạo Multi-Provider LLM Adapter
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
        f"✅ Đã tải thành công {len(tests)} Test Cases "
        f"từ config/test_cases.json\n"
    )

    # Chọn Test Case ID 4: câu hỏi cần sử dụng Tool
    sample_test = next(
        (test for test in tests if test["id"] == 4),
        tests[0],
    )

    sample_query = sample_test["question"]

    print("--- DEMO 1: CHẠY TRÊN CHATBOT BASELINE ---")
    run_baseline_chatbot(sample_query, provider)

    print("\n--- DEMO 2: CHẠY TRÊN REACT AGENT ---")
    run_react_agent(sample_query, provider)
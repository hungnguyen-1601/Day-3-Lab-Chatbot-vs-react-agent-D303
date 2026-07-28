"""
🧠 CẤP ĐỘ 3: REACTIVE AGENT (ReAct Agent - Thought -> Action -> Observation)
Agent tư vấn khóa học biết suy nghĩ, tự quyết định gọi Tool tra cứu dữ liệu
khóa học thực tế và quan sát kết quả để đưa ra câu trả lời chính xác.
"""


# Định nghĩa Tool thực tế (đồng bộ với src/tools.py)
def search_courses(topic: str, level: str) -> str:
    """
    Tra cứu khóa học phù hợp theo chủ đề và trình độ của sinh viên.

    Args:
        topic (str): Chủ đề muốn học (Ví dụ: 'Python', 'AI').
        level (str): Trình độ hiện tại (Ví dụ: 'Cơ bản', 'Nâng cao').

    Returns:
        str: Danh sách khóa học phù hợp.
    """
    topic_lower = topic.lower()

    if "ai" in topic_lower or "trí tuệ nhân tạo" in topic_lower:
        return (
            "Các khóa học AI phù hợp:\n"
            "1. Machine Learning cơ bản - 6 tuần - Miễn phí\n"
            "2. Deep Learning nhập môn - 5 tuần - 450.000 VNĐ\n"
            "3. Xây dựng dự án AI thực tế - 4 tuần - 300.000 VNĐ"
        )

    return f"LỖI: Không tìm thấy khóa học phù hợp với chủ đề '{topic}'."


def check_course_prerequisites(course_name: str) -> str:
    """
    Kiểm tra kiến thức đầu vào của một khóa học.

    Args:
        course_name (str): Tên khóa học cần kiểm tra.

    Returns:
        str: Thông tin về điều kiện đầu vào của khóa học.
    """
    course_lower = course_name.lower()

    if "deep learning" in course_lower:
        return (
            "Khóa Deep Learning nhập môn:\n"
            "- Yêu cầu biết Python\n"
            "- Đã học Machine Learning cơ bản\n"
            "- Biết kiến thức Đại số tuyến tính cơ bản"
        )

    return f"LỖI: Không tìm thấy thông tin khóa học '{course_name}'."


def reactive_agent_step(user_goal: str) -> None:
    """
    Mô phỏng một vòng lặp ReAct: Thought -> Action -> Observation.

    Args:
        user_goal (str): Yêu cầu tư vấn của người dùng.
    """
    print(f"🎯 Goal: {user_goal}")

    # Bước 1: Thought & Action gọi tool tra cứu khóa học
    print("\n🧠 [Thought 1]: Người dùng muốn học Deep Learning, "
          "tôi cần tra cứu khóa học thực tế trước.")
    print("🛠️ [Action 1] : search_courses('AI', 'Cơ bản')")
    obs1 = search_courses("AI", "Cơ bản")
    print(f"👁️ [Observation 1]:\n{obs1}")

    # Bước 2: Thought & Action kiểm tra điều kiện đầu vào
    print("\n🧠 [Thought 2]: Đã tìm thấy khóa Deep Learning nhập môn, "
          "cần kiểm tra điều kiện đầu vào.")
    print("🛠️ [Action 2] : check_course_prerequisites('Deep Learning nhập môn')")
    obs2 = check_course_prerequisites("Deep Learning nhập môn")
    print(f"👁️ [Observation 2]:\n{obs2}")

    # Bước 3: Thought & Final Answer
    print("\n🧠 [Thought 3]: Đã có đủ thông tin khóa học và điều kiện "
          "đầu vào. Đưa ra câu trả lời cuối cùng.")
    print(
        "🏁 [Final Answer]: Bạn có thể học khóa Deep Learning nhập môn "
        "trong 5 tuần với học phí 450.000 VNĐ. Điều kiện đầu vào là "
        "biết Python, đã học Machine Learning cơ bản và có kiến thức "
        "Đại số tuyến tính cơ bản."
    )


if __name__ == "__main__":
    print("=== DEMO CẤP ĐỘ 3: REACTIVE AGENT (ReAct Loop) ===")
    reactive_agent_step(
        "Tôi biết Python và đã học Machine Learning cơ bản, "
        "tôi muốn học Deep Learning thì cần điều kiện gì?"
    )

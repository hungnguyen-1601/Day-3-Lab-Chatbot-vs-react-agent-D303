"""
🛠️ TOOL REGISTRY & SCHEMAS (Dành cho Role 2: Tool & Spec Engineer)
Nơi khai báo tất cả các "món đồ nghề" mà ReAct Agent có thể gọi.
"""


def search_courses(topic: str, level: str) -> str:
    """
    Tra cứu khóa học phù hợp theo chủ đề và trình độ của sinh viên.

    Args:
        topic (str): Chủ đề muốn học
                     (Ví dụ: 'Python', 'AI', 'Machine Learning')
        level (str): Trình độ hiện tại
                     (Ví dụ: 'Cơ bản', 'Trung cấp', 'Nâng cao')

    Returns:
        str: Danh sách khóa học phù hợp
    """
    topic_lower = topic.lower()
    level_lower = level.lower()

    if "python" in topic_lower:
        return (
            "Các khóa học Python phù hợp:\n"
            "1. Python cơ bản - 4 tuần - Miễn phí\n"
            "2. Python cho phân tích dữ liệu - 6 tuần - 350.000 VNĐ"
        )

    elif "machine learning" in topic_lower or "học máy" in topic_lower:
        if "cơ bản" in level_lower or "beginner" in level_lower:
            return (
                "Khóa học phù hợp: Machine Learning cơ bản\n"
                "- Thời lượng: 6 tuần\n"
                "- Học phí: Miễn phí\n"
                "- Yêu cầu: Biết Python cơ bản"
            )

        return (
            "Khóa học phù hợp: Machine Learning nâng cao\n"
            "- Thời lượng: 8 tuần\n"
            "- Học phí: 700.000 VNĐ\n"
            "- Yêu cầu: Đã học Machine Learning cơ bản"
        )

    elif "ai" in topic_lower or "trí tuệ nhân tạo" in topic_lower:
        return (
            "Các khóa học AI phù hợp:\n"
            "1. Machine Learning cơ bản - 6 tuần - Miễn phí\n"
            "2. Deep Learning nhập môn - 5 tuần - 450.000 VNĐ\n"
            "3. Xây dựng dự án AI thực tế - 4 tuần - 300.000 VNĐ"
        )

    else:
        return f"LỖI: Không tìm thấy khóa học phù hợp với chủ đề '{topic}'."


def check_course_prerequisites(course_name: str) -> str:
    """
    Kiểm tra kiến thức đầu vào của một khóa học.

    Args:
        course_name (str): Tên khóa học cần kiểm tra
                           (Ví dụ: 'Machine Learning cơ bản')

    Returns:
        str: Thông tin về điều kiện đầu vào của khóa học
    """
    course_lower = course_name.lower()

    if "python cơ bản" in course_lower:
        return (
            "Khóa Python cơ bản:\n"
            "- Không yêu cầu kiến thức lập trình trước đó\n"
            "- Phù hợp với sinh viên mới bắt đầu"
        )

    elif "machine learning" in course_lower:
        return (
            "Khóa Machine Learning cơ bản:\n"
            "- Yêu cầu biết Python cơ bản\n"
            "- Nên biết kiến thức Toán và Xác suất cơ bản"
        )

    elif "deep learning" in course_lower:
        return (
            "Khóa Deep Learning nhập môn:\n"
            "- Yêu cầu biết Python\n"
            "- Đã học Machine Learning cơ bản\n"
            "- Biết kiến thức Đại số tuyến tính cơ bản"
        )

    elif "dự án ai" in course_lower:
        return (
            "Khóa Xây dựng dự án AI thực tế:\n"
            "- Yêu cầu biết Python\n"
            "- Đã học Machine Learning cơ bản"
        )

    else:
        return f"LỖI: Không tìm thấy thông tin khóa học '{course_name}'."


# Danh sách các tool được đăng ký để Agent sử dụng
AVAILABLE_TOOLS = {
    "search_courses": search_courses,
    "check_course_prerequisites": check_course_prerequisites,
}
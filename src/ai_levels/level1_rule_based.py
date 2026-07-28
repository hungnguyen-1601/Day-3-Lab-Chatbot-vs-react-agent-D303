"""
🤖 CẤP ĐỘ 1: RULE-BASED BOT
Chatbot tư vấn khóa học dựa trên luật if/else cố định.
Bot chỉ khớp từ khóa với câu trả lời có sẵn, không sử dụng LLM hoặc Tools.
"""


def rule_based_bot(user_input: str) -> str:
    """
    Trả lời câu hỏi tư vấn khóa học bằng các luật từ khóa cố định.

    Args:
        user_input (str): Câu hỏi của người dùng.

    Returns:
        str: Câu trả lời tương ứng với từ khóa đã được định nghĩa.
    """
    text = user_input.lower().strip()

    if not text:
        return "Vui lòng nhập câu hỏi để tôi có thể hỗ trợ bạn."

    if "chào" in text or "hello" in text or text == "hi":
        return (
            "Xin chào! Tôi là Rule-Based Bot tư vấn khóa học. "
            "Bạn muốn tìm hiểu về Python, Machine Learning, Deep Learning hay AI?"
        )

    elif "python" in text:
        return (
            "Khóa Python cơ bản kéo dài 4 tuần, miễn phí và phù hợp "
            "với sinh viên chưa có kinh nghiệm lập trình."
        )

    elif "machine learning" in text or "học máy" in text:
        return (
            "Khóa Machine Learning cơ bản kéo dài 6 tuần và miễn phí. "
            "Điều kiện đầu vào là biết Python cơ bản."
        )

    elif "deep learning" in text or "học sâu" in text:
        return (
            "Khóa Deep Learning nhập môn kéo dài 5 tuần, "
            "học phí 450.000 VNĐ. Bạn cần biết Python và "
            "đã học Machine Learning cơ bản."
        )

    elif "ai" in text or "trí tuệ nhân tạo" in text:
        return (
            "Để bắt đầu học AI, bạn nên học theo thứ tự: "
            "Python → Machine Learning → Deep Learning → Dự án AI thực tế."
        )

    elif (
        "học phí" in text
        or "chi phí" in text
        or "giá" in text
    ):
        return (
            "Học phí tham khảo: Python cơ bản miễn phí, "
            "Machine Learning cơ bản miễn phí và "
            "Deep Learning nhập môn 450.000 VNĐ."
        )

    elif "điều kiện" in text or "đầu vào" in text:
        return (
            "Python cơ bản không yêu cầu kiến thức đầu vào. "
            "Machine Learning yêu cầu biết Python. "
            "Deep Learning yêu cầu biết Python và Machine Learning cơ bản."
        )

    elif "liên hệ" in text or "hotline" in text:
        return (
            "Hotline hỗ trợ: 1900-1234. "
            "Email: support@vinuni.edu.vn"
        )

    else:
        return (
            "Xin lỗi, câu hỏi của bạn nằm ngoài tập luật được cài đặt sẵn. "
            "Bạn có thể hỏi về Python, Machine Learning, Deep Learning, "
            "AI, học phí hoặc điều kiện đầu vào."
        )


if __name__ == "__main__":
    print("=== DEMO CẤP ĐỘ 1: RULE-BASED BOT ===")

    test_queries = [
        "Chào bạn",
        "Tôi muốn học AI",
        "Khóa Machine Learning yêu cầu gì?",
        "Học phí Deep Learning là bao nhiêu?",
        "Tôi muốn học phép thuật",
    ]

    for query in test_queries:
        print(f"User: {query}")
        print(f"Bot : {rule_based_bot(query)}\n")
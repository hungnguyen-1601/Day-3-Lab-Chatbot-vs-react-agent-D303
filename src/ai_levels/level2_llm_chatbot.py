"""
🤖 CẤP ĐỘ 2: LLM CHATBOT (Baseline Chatbot không có Tool)
Chatbot tư vấn khóa học dùng LLM sinh câu trả lời tự nhiên, mượt mà hơn Cấp độ 1.
Tuy nhiên bot không có Tool nên không thể tra cứu dữ liệu khóa học thực tế
(học phí, thời lượng, điều kiện đầu vào chính xác).
"""

CHATBOT_BASELINE_PROMPT = """Bạn là một Chatbot tư vấn khóa học cho sinh viên.
Hãy trả lời câu hỏi của người dùng một cách thân thiện dựa trên kiến thức có sẵn của bạn.
Nếu không có thông tin cụ thể về khóa học, học phí, thời lượng hoặc điều kiện đầu vào,
hãy lịch sự thông báo rằng bạn không thể kiểm tra dữ liệu thực tế.
"""


def llm_chatbot(user_input: str) -> str:
    """
    Mô phỏng LLM trả lời câu hỏi tư vấn khóa học (không có Tool).

    Args:
        user_input (str): Câu hỏi của người dùng.

    Returns:
        str: Câu trả lời tự nhiên do LLM sinh ra, nhưng không có
             dữ liệu thực tế về khóa học.
    """
    text = user_input.lower().strip()

    if not text:
        return "🤖 [LLM Chatbot]: Vui lòng nhập câu hỏi để tôi có thể hỗ trợ bạn."

    # LLM không có Tool nên không thể tra cứu dữ liệu thực tế
    if (
        "học phí" in text
        or "chi phí" in text
        or "giá" in text
        or "lịch khai giảng" in text
        or "điều kiện" in text
        or "đầu vào" in text
    ):
        return (
            "🤖 [LLM Chatbot]: Tôi là AI hội thoại nhưng không được cấp "
            "công cụ tra cứu dữ liệu khóa học thực tế, nên tôi không thể "
            "kiểm tra chính xác học phí, lịch khai giảng hay điều kiện "
            "đầu vào hiện tại. Bạn vui lòng liên hệ phòng đào tạo để "
            "được xác nhận thông tin mới nhất nhé!"
        )

    if "ai" in text or "trí tuệ nhân tạo" in text or "machine learning" in text:
        return (
            "🤖 [LLM Chatbot]: Để học AI, bạn nên bắt đầu từ Python, "
            "sau đó học Machine Learning rồi Deep Learning. Đây là lộ "
            "trình phổ biến, tuy nhiên tôi không thể kiểm tra danh sách "
            "khóa học đang mở thực tế vì không có công cụ tra cứu."
        )

    return (
        f"🤖 [LLM Chatbot]: Rất vui được hỗ trợ bạn về câu hỏi "
        f"'{user_input}'! Tôi có thể tư vấn định hướng học tập chung, "
        f"nhưng không thể tra cứu dữ liệu khóa học thời gian thực."
    )


if __name__ == "__main__":
    print("=== DEMO CẤP ĐỘ 2: LLM CHATBOT BASELINE ===")

    test_queries = [
        "Tôi muốn học AI thì bắt đầu từ đâu?",
        "Học phí khóa Deep Learning là bao nhiêu?",
    ]

    for query in test_queries:
        print(f"User: {query}")
        print(f"Bot : {llm_chatbot(query)}\n")

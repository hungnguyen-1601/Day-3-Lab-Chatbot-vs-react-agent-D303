"""
🚀 CẤP ĐỘ 4: AUTONOMOUS AGENT (Agent tự chủ với Planning & Memory)
Agent tư vấn khóa học tự chia nhỏ mục tiêu phức tạp thành nhiều bước,
duy trì bộ nhớ (Memory) và tự đánh giá tiến độ để xây dựng lộ trình học.
"""


class AutonomousGoalAgent:
    """
    Agent tự chủ lập kế hoạch lộ trình học cho sinh viên.

    Attributes:
        goal (str): Mục tiêu học tập của người dùng.
        max_steps (int): Số vòng lặp tối đa (Guardrail chống lặp vô tận).
        memory (list): Bộ nhớ lưu vết các bước đã thực hiện.
    """

    def __init__(self, goal: str, max_steps: int = 4):
        self.goal = goal
        self.max_steps = max_steps
        self.memory = []  # Bộ nhớ lưu vết các bước đã thực hiện

    def execute(self) -> None:
        """
        Chạy vòng lặp tự chủ: Planning -> Execution -> Memory -> Evaluation.
        """
        print(f"🚀 === Bắt đầu Autonomous Goal: {self.goal} ===")

        for step in range(1, self.max_steps + 1):
            print(
                f"\n--- Vòng lặp tự chủ Planning & Action "
                f"(Step {step}/{self.max_steps}) ---"
            )

            if step == 1:
                plan = "Bước 1: Tra cứu các khóa học AI phù hợp với trình độ"
                action = "Call Tool: search_courses('AI', 'Cơ bản')"
                result = (
                    "Tìm thấy 3 khóa: Machine Learning cơ bản (miễn phí), "
                    "Deep Learning nhập môn (450.000 VNĐ), "
                    "Dự án AI thực tế (300.000 VNĐ)."
                )
            elif step == 2:
                plan = "Bước 2: Kiểm tra điều kiện đầu vào từng khóa học"
                action = (
                    "Call Tool: check_course_prerequisites"
                    "('Machine Learning cơ bản')"
                )
                result = (
                    "Machine Learning cơ bản yêu cầu biết Python. "
                    "Người dùng đã đạt điều kiện."
                )
            elif step == 3:
                plan = "Bước 3: Tổng hợp lộ trình học AI theo thứ tự hợp lý"
                action = "Generate Learning Roadmap"
                result = (
                    "Lộ trình hoàn tất: Machine Learning cơ bản (6 tuần) "
                    "→ Deep Learning nhập môn (5 tuần) "
                    "→ Dự án AI thực tế (4 tuần)."
                )
            else:
                print("🎯 [Goal Evaluation]: Mục tiêu đã hoàn thành 100%!")
                break

            self.memory.append(
                {"step": step, "plan": plan, "result": result}
            )
            print(f"📋 [Planning]: {plan}")
            print(f"🛠️ [Execution]: {action} ➔ {result}")
            print(f"💾 [Memory Saved]: Logged step {step} to memory.")


if __name__ == "__main__":
    print("=== DEMO CẤP ĐỘ 4: AUTONOMOUS AGENT (Planning & Memory) ===")
    agent = AutonomousGoalAgent(
        "Xây dựng lộ trình học AI cho sinh viên đã biết Python cơ bản"
    )
    agent.execute()

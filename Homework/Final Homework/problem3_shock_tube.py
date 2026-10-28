import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


gamma = 1.4
rho4 = 1.0
p4 = 100000.0
u4 = 0.0
rho1 = 0.125
p1 = 10000.0
u1 = 0.0
t_final = 0.01


def expansion_velocity(p_star: float) -> float:
    a4 = math.sqrt(gamma * p4 / rho4)
    exponent = (gamma - 1.0) / (2.0 * gamma)
    return u4 + 2.0 * a4 / (gamma - 1.0) * (1.0 - (p_star / p4) ** exponent)


def shock_velocity_relation(p_star: float) -> float:
    factor = math.sqrt(
        (2.0 / ((gamma + 1.0) * rho1))
        / (p_star + ((gamma - 1.0) / (gamma + 1.0)) * p1)
    )
    return u1 + (p_star - p1) * factor


def pressure_residual(p_star: float) -> float:
    return expansion_velocity(p_star) - shock_velocity_relation(p_star)


def bisect_root(lo: float, hi: float, tol: float = 1e-10, max_iter: int = 200) -> float:
    f_lo = pressure_residual(lo)
    f_hi = pressure_residual(hi)
    if f_lo * f_hi > 0:
        raise ValueError("Root is not bracketed")
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        f_mid = pressure_residual(mid)
        if abs(f_mid) < tol or abs(hi - lo) < tol:
            return mid
        if f_lo * f_mid <= 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    return 0.5 * (lo + hi)


a4 = math.sqrt(gamma * p4 / rho4)
a1 = math.sqrt(gamma * p1 / rho1)
p_star = bisect_root(p1, p4)
u_star = expansion_velocity(p_star)
rho3 = rho4 * (p_star / p4) ** (1.0 / gamma)
a3 = a4 * (p_star / p4) ** ((gamma - 1.0) / (2.0 * gamma))
pressure_ratio = p_star / p1
rho2 = rho1 * (
    (pressure_ratio + ((gamma - 1.0) / (gamma + 1.0)))
    / (1.0 + ((gamma - 1.0) / (gamma + 1.0)) * pressure_ratio)
)
a2 = math.sqrt(gamma * p_star / rho2)
u_s = rho2 * u_star / (rho2 - rho1)

xi_head = u4 - a4
xi_tail = u_star - a3
x_head = xi_head * t_final
x_tail = xi_tail * t_final
x_contact = u_star * t_final
x_shock = u_s * t_final


def fan_state(xi: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    a = (gamma - 1.0) / (gamma + 1.0) * (u4 + 2.0 * a4 / (gamma - 1.0) - xi)
    u = xi + a
    rho = rho4 * (a / a4) ** (2.0 / (gamma - 1.0))
    p = p4 * (a / a4) ** (2.0 * gamma / (gamma - 1.0))
    return rho, u, p


def solution_at(x: np.ndarray, t: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    xi = x / t
    rho = np.empty_like(x)
    u = np.empty_like(x)
    p = np.empty_like(x)

    mask4 = xi < xi_head
    mask_fan = (xi >= xi_head) & (xi <= xi_tail)
    mask3 = (xi > xi_tail) & (xi < u_star)
    mask2 = (xi >= u_star) & (xi < u_s)
    mask1 = xi >= u_s

    rho[mask4] = rho4
    u[mask4] = u4
    p[mask4] = p4

    rho[mask_fan], u[mask_fan], p[mask_fan] = fan_state(xi[mask_fan])

    rho[mask3] = rho3
    u[mask3] = u_star
    p[mask3] = p_star

    rho[mask2] = rho2
    u[mask2] = u_star
    p[mask2] = p_star

    rho[mask1] = rho1
    u[mask1] = u1
    p[mask1] = p1

    return rho, u, p


out_dir = Path("Homework/Final Homework/images")
out_dir.mkdir(parents=True, exist_ok=True)

x_min = -4.5
x_max = 6.2

x = np.linspace(x_min, x_max, 2600)
rho, u, p = solution_at(x, t_final)

fig, axes = plt.subplots(3, 1, figsize=(8.2, 8.4), sharex=True)
axes[0].plot(x, rho, color="#1f77b4", linewidth=2)
axes[0].set_ylabel(r"$\rho\;[\mathrm{kg/m^3}]$")
axes[1].plot(x, u, color="#d62728", linewidth=2)
axes[1].set_ylabel(r"$u\;[\mathrm{m/s}]$")
axes[2].plot(x, p, color="#2ca02c", linewidth=2)
axes[2].set_ylabel(r"$p\;[\mathrm{Pa}]$")
axes[2].set_xlabel(r"$x\;[\mathrm{m}]$")
for ax in axes:
    ax.grid(True, alpha=0.25)
    for loc, style, color in [
        (x_head, ":", "#777777"),
        (x_tail, ":", "#777777"),
        (x_contact, "--", "#111111"),
        (x_shock, "-", "#111111"),
    ]:
        ax.axvline(loc, linestyle=style, color=color, linewidth=1.1, alpha=0.8)
axes[0].set_title(r"Shock-tube solution at $t=0.01\,\mathrm{s}$")
axes[0].text(x_head, axes[0].get_ylim()[1] * 0.92, "fan head", rotation=90, va="top", ha="right", fontsize=8)
axes[0].text(x_tail, axes[0].get_ylim()[1] * 0.92, "fan tail", rotation=90, va="top", ha="left", fontsize=8)
axes[0].text(x_contact, axes[0].get_ylim()[1] * 0.92, "contact", rotation=90, va="top", ha="left", fontsize=8)
axes[0].text(x_shock, axes[0].get_ylim()[1] * 0.92, "shock", rotation=90, va="top", ha="left", fontsize=8)
fig.tight_layout()
state_plot = out_dir / "problem3_state_profiles.png"
fig.savefig(state_plot, dpi=200)
plt.close(fig)


def cplus_in_fan(tau: np.ndarray, tau0: float) -> np.ndarray:
    # A C+ characteristic entering the fan at tau0 from the fan head.
    # In the fan, xi=x/t, xi=u-a, and dx/dt=u+a.
    # Solving t dxi/dt + xi = u+a gives
    # 2a4-(gamma-1)xi = C*t^{-2(gamma-1)/(gamma+1)}.
    power = 2.0 * (gamma - 1.0) / (gamma + 1.0)
    c = (2.0 * a4 - (gamma - 1.0) * xi_head) * tau0**power
    xi = (2.0 * a4 - c * tau ** (-power)) / (gamma - 1.0)
    return xi * tau


fig, ax = plt.subplots(figsize=(8.0, 6.2))
t_vals = np.linspace(0.0, t_final, 300)
t_pos = np.linspace(1e-5, t_final, 300)


def plot_masked_line(axis, x_line, t_line, mask, **kwargs) -> None:
    indices = np.where(mask)[0]
    if len(indices) == 0:
        return
    splits = np.where(np.diff(indices) > 1)[0] + 1
    for group in np.split(indices, splits):
        if len(group) > 1:
            axis.plot(x_line[group], t_line[group], **kwargs)


# Wave boundaries.
ax.plot(xi_head * t_vals, t_vals, color="black", linestyle=":", linewidth=1.5, label="fan head/tail")
ax.plot(xi_tail * t_vals, t_vals, color="black", linestyle=":", linewidth=1.5)
ax.plot(u_star * t_vals, t_vals, color="black", linestyle="--", linewidth=1.8, label="contact")
ax.plot(u_s * t_vals, t_vals, color="black", linestyle="-", linewidth=2.0, label="shock")

# C- expansion fan rays.
for xi in np.linspace(xi_head, xi_tail, 13):
    ax.plot(xi * t_vals, t_vals, color="#d62728", linewidth=1.0, alpha=0.75)

# Uniform-region characteristics.
for x0 in np.linspace(x_min + 0.2, -0.4, 9):
    x_plus = x0 + (u4 + a4) * t_vals
    x_minus = x0 + (u4 - a4) * t_vals
    plot_masked_line(ax, x_plus, t_vals, x_plus <= xi_head * t_vals, color="#1f77b4", linewidth=0.9, alpha=0.45)
    plot_masked_line(ax, x_minus, t_vals, x_minus <= xi_head * t_vals, color="#d62728", linewidth=0.9, alpha=0.35)

for tau0 in np.linspace(0.0018, 0.009, 5):
    t_curve = np.linspace(tau0, t_final, 160)
    x_curve = cplus_in_fan(t_curve, tau0)
    valid = (x_curve >= xi_head * t_curve) & (x_curve <= xi_tail * t_curve)
    ax.plot(x_curve[valid], t_curve[valid], color="#1f77b4", linewidth=1.2, alpha=0.85)
    if np.any(valid):
        t_exit = t_curve[valid][-1]
        x_exit = x_curve[valid][-1]
        t_after = np.linspace(t_exit, t_final, 80)
        x_after = x_exit + (u_star + a3) * (t_after - t_exit)
        plot_masked_line(
            ax,
            x_after,
            t_after,
            (x_after >= xi_tail * t_after) & (x_after <= u_star * t_after),
            color="#1f77b4",
            linewidth=1.0,
            alpha=0.55,
        )

for x0 in np.linspace(x_tail - 1.2, x_contact - 0.2, 4):
    x_plus = x0 + (u_star + a3) * t_vals
    x_minus = x0 + (u_star - a3) * t_vals
    mask_plus = (x_plus >= xi_tail * t_vals) & (x_plus <= u_star * t_vals)
    mask_minus = (x_minus >= xi_tail * t_vals) & (x_minus <= u_star * t_vals)
    plot_masked_line(ax, x_plus, t_vals, mask_plus, color="#1f77b4", linewidth=0.9, alpha=0.4)
    plot_masked_line(ax, x_minus, t_vals, mask_minus, color="#d62728", linewidth=0.9, alpha=0.35)

for x0 in np.linspace(x_contact + 0.15, x_shock - 0.2, 4):
    x_plus = x0 + (u_star + a2) * t_vals
    x_minus = x0 + (u_star - a2) * t_vals
    mask_plus = (x_plus >= u_star * t_vals) & (x_plus <= u_s * t_vals)
    mask_minus = (x_minus >= u_star * t_vals) & (x_minus <= u_s * t_vals)
    plot_masked_line(ax, x_plus, t_vals, mask_plus, color="#1f77b4", linewidth=0.9, alpha=0.4)
    plot_masked_line(ax, x_minus, t_vals, mask_minus, color="#d62728", linewidth=0.9, alpha=0.35)

for x0 in np.linspace(x_shock + 0.15, x_max - 0.2, 4):
    x_plus = x0 + (u1 + a1) * t_vals
    x_minus = x0 + (u1 - a1) * t_vals
    plot_masked_line(ax, x_plus, t_vals, x_plus >= u_s * t_vals, color="#1f77b4", linewidth=0.9, alpha=0.35)
    plot_masked_line(ax, x_minus, t_vals, x_minus >= u_s * t_vals, color="#d62728", linewidth=0.9, alpha=0.35)

ax.text(-4.0, 0.0085, "Region 4", fontsize=9)
ax.text((x_tail + x_contact) / 2, 0.0085, "Region 3", fontsize=9, ha="center")
ax.text((x_contact + x_shock) / 2, 0.0085, "Region 2", fontsize=9, ha="center")
ax.text(5.85, 0.0085, "Region 1", fontsize=9, ha="center")
ax.text((x_head + x_tail) / 2, 0.0045, "expansion fan", fontsize=9, rotation=20, ha="center")
ax.set_xlim(x_min, x_max)
ax.set_ylim(0.0, t_final)
ax.set_xlabel(r"$x\;[\mathrm{m}]$")
ax.set_ylabel(r"$t\;[\mathrm{s}]$")
ax.set_title(r"Shock-tube characteristic structure")
ax.grid(True, alpha=0.25)
ax.plot([], [], color="#1f77b4", label=r"$C_+$")
ax.plot([], [], color="#d62728", label=r"$C_-$")
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()
char_plot = out_dir / "problem3_characteristics.png"
fig.savefig(char_plot, dpi=200)
plt.close(fig)

print(f"a4={a4:.10f}")
print(f"a1={a1:.10f}")
print(f"p_star={p_star:.10f}")
print(f"u_star={u_star:.10f}")
print(f"rho3={rho3:.10f}")
print(f"a3={a3:.10f}")
print(f"rho2={rho2:.10f}")
print(f"a2={a2:.10f}")
print(f"u_s={u_s:.10f}")
print(f"xi_head={xi_head:.10f}")
print(f"xi_tail={xi_tail:.10f}")
print(f"x_head={x_head:.10f}")
print(f"x_tail={x_tail:.10f}")
print(f"x_contact={x_contact:.10f}")
print(f"x_shock={x_shock:.10f}")
print(state_plot)
print(char_plot)

fig, ax = plt.subplots(figsize=(8.0, 4.8))
t_vals = np.linspace(0.0, t_final, 300)
ax.fill_betweenx(
    t_vals,
    xi_head * t_vals,
    xi_tail * t_vals,
    color="#d62728",
    alpha=0.15,
    label="expansion fan",
)
ax.plot(xi_head * t_vals, t_vals, color="#d62728", linestyle=":", linewidth=1.8)
ax.plot(xi_tail * t_vals, t_vals, color="#d62728", linestyle=":", linewidth=1.8)
ax.plot(u_star * t_vals, t_vals, color="black", linestyle="--", linewidth=2.0, label="contact")
ax.plot(u_s * t_vals, t_vals, color="black", linestyle="-", linewidth=2.2, label="shock")
ax.text(-3.8, 0.008, "Region 4", ha="center", fontsize=10)
ax.text((x_tail + x_contact) / 2, 0.008, "Region 3", ha="center", fontsize=10)
ax.text((x_contact + x_shock) / 2, 0.008, "Region 2", ha="center", fontsize=10)
ax.text(5.85, 0.008, "Region 1", ha="center", fontsize=10)
ax.text((x_head + x_tail) / 2, 0.004, "expansion fan", rotation=20, ha="center", fontsize=10)
label_t = 0.0055
ax.text(u_star * label_t + 0.12, label_t, "contact", rotation=62, fontsize=9)
ax.text(u_s * label_t + 0.12, label_t, "shock", rotation=58, fontsize=9)
ax.set_xlim(x_min, x_max)
ax.set_ylim(0.0, t_final)
ax.set_xlabel(r"$x\;[\mathrm{m}]$")
ax.set_ylabel(r"$t\;[\mathrm{s}]$")
ax.set_title(r"Shock-tube wave structure")
ax.grid(True, alpha=0.25)
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()
wave_plot = out_dir / "problem3_wave_structure.png"
fig.savefig(wave_plot, dpi=200)
plt.close(fig)
print(wave_plot)

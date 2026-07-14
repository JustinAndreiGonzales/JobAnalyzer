package com.justin.JobAnalyzerBE.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
@AllArgsConstructor
public class UserProfile {
    @OneToOne
    @JoinColumn(name = "user_id")
    private User user;
    private String firstName;
    private String lastName;

    private String targetRole;
    private String employmentType;
    private String workSetup;

    private Integer expectedSalaryMin;
    private Integer expectedSalaryMax;

    private String experienceLevel;

    @Column(length = 3000)
    private String summary;
}
